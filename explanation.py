def generate_explanation(skill_name, skill):
    demand = skill["demand"]
    salary = skill["salary"]
    growth = skill["growth"]
    automation = skill["automation_risk"]
    alternative = skill["alternative"]

    # Score calculation
    avg_score = (demand + salary + growth) / 3

    # Decision logic
    if avg_score < 5 or automation >= 7:
        decision = "Avoid ❌"
    elif avg_score < 7:
        decision = "Moderate ⚠️"
    else:
        decision = "Good to Learn ✅"

    # Build explanation
    reasons = []

    if demand < 5:
        reasons.append("low demand in the job market")
    if growth < 5:
        reasons.append("limited future growth")
    if automation >= 7:
        reasons.append("high risk of automation")
    if salary < 5:
        reasons.append("low salary potential")

    if decision.startswith("Avoid"):
        reason_text = f"Avoid {skill_name} because it has " + ", ".join(reasons) + "."
    else:
        reason_text = f"{skill_name} is a good skill due to strong demand, salary potential, and future growth."

    return {
        "skill": skill_name,
        "decision": decision,
        "reason": reason_text,
        "alternative": alternative,
        "score": round(avg_score, 2)
    }