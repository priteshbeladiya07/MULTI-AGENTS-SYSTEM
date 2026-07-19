import streamlit as st
import streamlit.components.v1 as components
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

st.set_page_config(page_title="Research Pipeline", layout="wide")


# Build agents once and reuse across runs (they don't depend on the topic)
@st.cache_resource
def get_agents():
    return build_search_agent(), build_reader_agent()


def research_animation(label: str, height: int = 210):
    """Renders a radar-sweep animation: a rotating scan line over a
    circular grid with pulsing blips (representing sources being found),
    with a status label underneath."""
    html = f"""
    <div style="display:flex;flex-direction:column;align-items:center;
                justify-content:center;font-family:sans-serif;padding:8px 0;">
      <style>
        @keyframes rs-rotate {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
        @keyframes rs-blip {{
          0%, 100% {{ opacity: 0; transform: scale(0.4); }}
          50%      {{ opacity: 1; transform: scale(1); }}
        }}
        @keyframes rs-dot {{ 0%, 100% {{ opacity: 0.2; }} 50% {{ opacity: 1; }} }}
        .rs-radar {{ position: relative; width: 140px; height: 140px; margin: 0 auto; }}
        .rs-ring {{ position: absolute; border: 1px solid rgba(99,102,241,0.35); border-radius: 50%; }}
        .rs-ring.c1 {{ width: 100%; height: 100%; top: 0; left: 0; }}
        .rs-ring.c2 {{ width: 66%; height: 66%; top: 17%; left: 17%; }}
        .rs-ring.c3 {{ width: 33%; height: 33%; top: 33%; left: 33%; }}
        .rs-sweep {{
          position: absolute; width: 50%; height: 50%; top: 0; left: 50%;
          background: conic-gradient(from 0deg, rgba(99,102,241,0.55), transparent 70deg);
          transform-origin: 0% 100%; border-radius: 0 100% 0 0;
          animation: rs-rotate 2.2s linear infinite;
        }}
        .rs-blip {{
          position: absolute; width: 8px; height: 8px; background: #6366f1;
          border-radius: 50%; animation: rs-blip 2.4s ease-in-out infinite;
        }}
        .rs-center {{
          position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
          font-size: 20px;
        }}
        .rs-label {{ margin-top: 8px; font-size: 13px; color: #6366f1; font-weight: 500; }}
        .rs-lbl-dot {{ animation: rs-dot 1.2s infinite; }}
        .rs-lbl-dot:nth-child(2) {{ animation-delay: 0.2s; }}
        .rs-lbl-dot:nth-child(3) {{ animation-delay: 0.4s; }}
      </style>
      <div class="rs-radar">
        <div class="rs-ring c1"></div>
        <div class="rs-ring c2"></div>
        <div class="rs-ring c3"></div>
        <div class="rs-sweep"></div>
        <div class="rs-blip" style="top:22%; left:65%; animation-delay:0.0s;"></div>
        <div class="rs-blip" style="top:60%; left:75%; animation-delay:0.6s;"></div>
        <div class="rs-blip" style="top:70%; left:30%; animation-delay:1.2s;"></div>
        <div class="rs-blip" style="top:30%; left:20%; animation-delay:1.8s;"></div>
        <div class="rs-center">🔎</div>
      </div>
      <div class="rs-label">{label}<span class="rs-lbl-dot">.</span><span class="rs-lbl-dot">.</span><span class="rs-lbl-dot">.</span></div>
    </div>
    """
    components.html(html, height=height)


def run_pipeline_ui(topic: str):
    state = {}
    search_agent, reader_agent = get_agents()

    # Step 1 - Search
    with st.status("Step 1 — Searching...", expanded=True) as status:
        anim = st.empty()
        with anim:
            research_animation("Searching the web")
        search_result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
        })
        anim.empty()
        state["search_results"] = search_result["messages"][-1].content
        status.update(label="Step 1 — Search done", state="complete")

    with st.expander("Search Results", expanded=False):
        st.write(state["search_results"])

    # Step 2 - Reader
    with st.status("Step 2 — Reading top source...", expanded=True) as status:
        anim = st.empty()
        with anim:
            research_animation("Scraping source")
        reader_result = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}"
            )]
        })
        anim.empty()
        state["scraped_content"] = reader_result["messages"][-1].content
        status.update(label="Step 2 — Reading done", state="complete")

    with st.expander("Scraped Content", expanded=False):
        st.write(state["scraped_content"])

    # Step 3 - Writer
    with st.status("Step 3 — Drafting report...", expanded=True) as status:
        anim = st.empty()
        with anim:
            research_animation("Writing report")
        research_combined = (
            f"SEARCH RESULTS : \n {state['search_results']} \n\n"
            f"DETAILED SCRAPED CONTENT : \n {state['scraped_content']}"
        )
        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })
        anim.empty()
        status.update(label="Step 3 — Report drafted", state="complete")

    # Step 4 - Critic
    with st.status("Step 4 — Critic reviewing...", expanded=True) as status:
        anim = st.empty()
        with anim:
            research_animation("Reviewing report")
        state["feedback"] = critic_chain.invoke({"report": state["report"]})
        anim.empty()
        status.update(label="Step 4 — Review done", state="complete")

    return state


def main():
    st.title("Multi-Agent Research Pipeline")

    if "state" not in st.session_state:
        st.session_state.state = None

    with st.sidebar:
        topic = st.text_input("Research topic", placeholder="e.g. quantum computing in 2026")
        run_clicked = st.button("Run pipeline", type="primary", disabled=not topic)

    if run_clicked and topic:
        st.session_state.state = run_pipeline_ui(topic)

    state = st.session_state.state
    if state:
        st.divider()
        tab_report, tab_feedback, tab_raw = st.tabs(["Report", "Critic Feedback", "Raw Data"])

        with tab_report:
            st.markdown(state["report"])
            st.download_button(
                "Download report",
                data=str(state["report"]),
                file_name="report.md",
                mime="text/markdown",
            )

        with tab_feedback:
            st.markdown(state["feedback"])

        with tab_raw:
            st.subheader("Search Results")
            st.write(state["search_results"])
            st.subheader("Scraped Content")
            st.write(state["scraped_content"])
    else:
        st.divider()
        research_animation("Waiting for a topic")
        st.caption("Enter a topic in the sidebar and click 'Run pipeline' to start.")


if __name__ == "__main__":
    main()