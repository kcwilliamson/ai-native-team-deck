"""One rule for how the deck moves between slides.

Big moves mark a change of section, small moves happen inside one:
  pixel  squares  -> entering a Phase (Play, Build, Design)
  blinds bars     -> entering a group (The divide, Before, After, Q&A)
  scan   sweep    -> a sub-section (Concerns -> Goals, Result -> Lessons) and "Where this goes next"
  soft   slide    -> every slide inside a section (header stays put, content eases over)
"""
def group(s):
    return s.split(' · ')[0]

def auto_tx(labels):
    out = []
    for i, s in enumerate(labels):
        if i == 0:
            out.append('cover'); continue
        p = labels[i - 1]
        if group(s) != group(p):
            g = group(s)
            out.append('pixel' if g.startswith('Phase') else 'scan' if g == 'Where this goes next' else 'blinds')
        elif s != p:
            out.append('scan')
        else:
            out.append('soft')
    return out
