from state import jobagentstate

def explanation_agent(state : jobagentstate) ->jobagentstate:
    match = state["match_result"]

    score = match.get("match_score", 0)
    matched = match.get("matched_skill", [])
    missing = match.get("missing_skill", [])

    explanation = f"""
Match Score: {score}%

You are a good fit because you have these required skills:
{', '.join(matched) if matched else 'None'}

You may improve your chances by adding or highlighting these skills:
{', '.join(missing) if missing else 'None'}
""".strip()

    state["explanation"] = explanation
    return state