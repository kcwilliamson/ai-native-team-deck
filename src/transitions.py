"""One rule for how the deck moves between slides.

Big moves mark a change of section, small moves happen inside one:
  pixel  squares  -> entering a Phase (Play, Build, Design)
  blinds bars     -> entering a group (The divide, Before, After, Q&A)
  scan   sweep    -> a sub-section (Concerns -> Goals, Result -> Lessons) and "Closing"
  soft   slide    -> every slide inside a section (header stays put, content eases over)
"""
def group(s):
    return s.split(' · ')[0]

# a slide that opens a titled section inside a group gets the bars, not the lighter scan
OVERRIDE = {43: 'blinds'}  # 'What we learned' (NEW SECTION card)

def auto_tx(labels, ids=None):
    out = []
    for i, s in enumerate(labels):
        if i == 0:
            out.append('cover'); continue
        p = labels[i - 1]
        if group(s) != group(p):
            g = group(s)
            out.append('pixel' if g.startswith('Phase') else 'scan' if g == 'Closing' else 'blinds')
        elif s != p:
            out.append(OVERRIDE.get(ids[i] if ids else None, 'scan'))
        else:
            out.append('soft')
    return out
