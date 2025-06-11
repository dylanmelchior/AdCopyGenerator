# build prompt
# 5 headlines 60-90
# 15 headlines 30 char
# 5 descriptions 90 char max
def build_prompt(company_info):
    return f"""  Based on the company info below, perform the following tasks and return the results in the exact format specified. Do not include section headers, labels, or any extra explanation.

Tasks:
Write one concise, simplified, focused, and compelling sales proposition (tagline) — this should clearly state the problem the company solves.

From that tagline, write 5 marketing headlines, each between 60–90 characters in length.

Then write 15 short headlines, each with a maximum of 30 characters. This is a strict maximum.

Then write 5 company descriptions, each with a maximum of 90 characters. This is a strict maximum.

Output format (strict):

Line 1: Tagline

Lines 2–6: 5 marketing headlines (60–90 characters)

Lines 7–21: 15 marketing headlines (Max 30 characters). These headlines should have title case.

Lines 22–26: 5 company descriptions (Max 90 characters)

Do not include any extra text, labels, numbers, or formatting beyond what is described above. Return only the 26 lines exactly.

Company Info:
{company_info}
    """