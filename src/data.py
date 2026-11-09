# slide number -> (title for reading view, transition into slide, drawer text)
T={ 'pixel':'Pixel blocks','blinds':'Blinds','scan':'Scan wipe','fade':'Quick fade','cover':'Cover builds in'}
D={
1:("AI-enabling a team","cover","Welcome. The chat is open the whole time, so drop questions in any time, silly ones first. A co-pilot (an AI helper) is watching it for me."),
2:("Stop with the jargon. Just talk to me.","fade","A rule from home: when work talk fills up with buzzwords, a hand goes up and someone says, \"Stop with the jargon. Just talk to me.\" Everyone in this room gets that hand today."),
3:("Goals. Play. Build. Design.","pixel","The route: how a team plays with AI, builds with it, then designs with it, plus the few things that go wrong along the way."),
4:("House rule: plain English","fade","AI took down the language barrier, so let's not rebuild it with vocabulary. Every AI term gets defined the first time it's used, and the chat is the place to say \"what does that mean?\""),
5:("Skeptical users. Nervous team. Gung-ho leadership. Racing market.","pixel","Our customers were highly technical and security-minded, so trust was fragile, and early chatbot experiments raised support tickets. On the team, people worried about the environment, made-up answers (hallucinations), brain rot, ethics, and being left behind or replaced. Leaders said this is the way, and the market was racing."),
6:("The divide","blinds","The skeptics and the racers weren't wrong. They just weren't talking to each other. Our customers were our team, and empathetic teams spot concerns fast, which is what you want when the market says ship AI now. It only works when people feel safe saying it out loud. That's psychological safety."),
7:("FOMO","fade","Keeping up made us nervous. The marketing is so good it creates a fear of missing out (FOMO) like nothing I'd seen. A technical program manager once asked me how to work with AI development. If that person feels behind, nobody is ahead."),
8:("Will I? becomes How well?","blinds","AI is no longer really an opt-out. I don't agree with \"use it or get out,\" but there will be a stark difference between people who learn to move quickly and well and people who don't. Waiting stopped being the safe choice."),
9:("Crossing together","scan","Skeptics and racers on the same goals, in plain language, with nobody gatekept out. Worries get heard, not dismissed, and the human stays in charge. This is where the talk is headed."),
10:("Four planks","scan","Four planks to cross: Goals, Play, Build, Design. We lay them one at a time, and look at what nearly collapsed the bridge along the way."),
11:("Four gotchas, four fixes","pixel","AI adoption tends to go wrong in four familiar ways. Each one has a fix you'll hear in the story."),
12:("Panic and false confidence","blinds","Coworkers raced each other, and the better they felt with AI, the harder they pushed. A whole design team changed its titles to design engineers within a month and left behind bad code and less thoughtful designs, because they couldn't see their own mistakes. Once titled as engineers they were judged as engineers, and a specialty was lost to panic. Engineering teams have AI too: what they need from design is good design, not more code. Everyone's skills get magnified by AI, not replaced."),
13:("Hype is jargon too","fade","Marketing hype is jargon too, and it's the glass ceiling all over again. In my experience, product teams run a handful of very specific agents on a build, not a swarm. Ask questions of big claims: what does it actually do?"),
14:("The worries we heard","fade","Psychological safety came first: people feel safe speaking up without being punished. We named the big worries out loud: environment, security, hallucinations, ethics, brain rot, and being left behind or replaced. We can't solve most of them, but we acknowledged all of them."),
15:("Goals before gadgets","pixel","Company goals were vague, so they didn't tell a team what to do on Monday. Every quarter I set specific OKRs for my team. An OKR is an objective plus the measurable results that show you got there. We looked at the roadmap, found the through-lines connecting the work, and set metrics combining product work with company objectives."),
16:("Goals, linked to outcomes","fade","Linking goals to outcomes answers the stakeholder question: why did you work on this? An AI experiment isn't a side hustle when it shows up in the same goals as the product work."),
17:("A real example","fade","Objective: create AI experiences that help customers find answers faster. Key results: improve search accuracy, keep customer sentiment positive, and check the box on AI. Team goals: level up on how AI really works, expand research to include AI, and evolve the team for a new future."),
18:("Play: sandbox before factory","pixel","I gave the team access to AI tools and one goal: find new ways to use AI. Low risk, low pressure, internal only. You don't learn to swim at the Olympics."),
19:("What the team actually did","fade","A shared prompt library for the most-used documents like PRDs and design specs (a prompt library is a set of tested instructions for the AI, like recipe cards). Drafting internal blogs and copyediting. Using AI as a sounding board. Testing which models and versions worked best for what, because not everything needs the biggest model. Trying new tools. One lesson: early chatbot experiments increased support tickets."),
20:("Share. Teach. Celebrate. Yes, and.","fade","Share: biweekly sprint reviews kept everyone in sync, nothing in the shadows. Teach what we did and why, so others reuse the thinking, not just copy the output. Celebrate: quarterly demos let everyone be seen. \"Yes, and\" is from improv: accept the idea, then add to it. It's how a napkin sketch becomes a team build."),
21:("Build: our own tools","pixel","We used AI to write code for internal products, tools our team and the wider company could use. The goal was reuse: one person's work became everyone's, and work that used to need a specialist opened up to more people. Nobody had to do it alone: we built off each other, worked with engineers or specialists when needed, and leaned on design thinking to solidify the thinking."),
22:("Three tools","fade","Feedback tool: pulls from community posts, support tickets, surveys and more, classifies them with AI, and shows a dashboard. Months of research became minutes. Content scorer: scores customer-facing words against the style rules, and one product area's average score rose by about a third. Papercut report: finds small usability problems in a systematic way, and led to dozens of improvements in record time."),
23:("From mundane to strategic","scan","Feedback: digging through scattered feedback became strategy conversations shaped by customer signal. Scorer: manual line edits became high-judgment feedback that shaped how the team approached design critique. Papercuts: hunting small problems by hand became a systematic way to find and prioritize, so time went to deciding what mattered."),
24:("The leadership shift","scan","Having data in hand is a powerful tool for conversation, and AI lets you grab it. Not being constantly in the weeds frees time for the bigger picture. Teams like ours often fight for a seat at the table, and with AI the fight got tougher, because every team felt they could jump over us with the speed and false confidence of AI. My proudest moment: one of my direct reports was invited into annual planning conversations."),
25:("Design: learn by doing","pixel","You don't know what AI can and can't do until you work with it. People who only have the theory often never start, and you can't learn to swim from a book. Because we built first, we knew where AI was strong and where it needed help."),
26:("Search: an answer, not a chat","fade","We watched users click through each product on the dashboard and fail to find things. We deliberately skipped an open-ended chatbot or agent. Instead we added an AI search bar with suggested prompts and made search lead to an answer, not a conversation. Customer sentiment held steady while product adoption rose."),
27:("Fix the source","fade","A hallucination is the AI confidently making something up. When accuracy dropped, the AI was pulling from the wrong material, and the more information an agent had, the less accurate it got. We fixed the source: format, tagging and chunking (breaking content into small labeled pieces the AI can find and use). Answers went from roughly one in five accurate to roughly four in five."),
28:("Enable, don't gatekeep","fade","Gatekeeping hoards the tool, the vocabulary or the reasoning. Enabling shares all three. Build tools so non-experts can do expert-level work with the human still in charge: people review the output and ask an expert when unsure. That's the line between enabling and the title flip: add skills, don't replace specialists."),
29:("No more chatbots","pixel","Ask AI how to build, but don't always jump to AI. Look for the pragmatic engineering first, because not everything needs an LLM (a large language model, the engine behind chat AI) or an agent. AI is how you learn to build, not always what you build. Before building a chatbot, ask: is this something Claude can't already do? Don't put the lift on the user to engage with a chatbot as the main interaction."),
30:("Find your value spots","fade","Human in the loop is about taste, creativity and authority. Don't worry about claiming tasks: the human superpower is talking to experts and making the judgment call. Prototyping is fast, cheap and easy, so treat what you bring back as a napkin sketch, then bring in the experts. Product development practice makes sure you build it with the right people and the right business case."),
31:("Almost no one is an expert","fade","Don't talk down to each other, and feel confident enough to ask others not to. Almost no one is an AI expert, except engineers building models at their core. When someone makes a big claim, ask what it does, who checked it, and how many moving parts it really needs. If you don't know, ask me or ask Copilot. It's fun to figure out."),
32:("Try 1: a prompt builds a site","pixel","Try it yourself: one prompt that creates a small local site. The prompt is on the slide so you can copy it."),
33:("Try 2: template + prompt","fade","Add a template, plus the prompt that created it, so anyone can reuse it. That's the prompt library idea made personal."),
34:("Try 3: presentation tips","fade","Ask Copilot for presentation tips, then pick the ones that fit on a slide. Same trick this talk used."),
35:("Set client AI goals together","fade","Use the same method with clients: start from their roadmap, find the through-lines together, and set one specific AI goal and one metric per engagement. Goals chosen on purpose, not bolted on because AI is in the news."),
36:("Questions?","blinds","Drop your questions in the chat. The best plain-English ones get answered live, and if jargon slips out I'll say so and restate it."),
37:("AI took down the language barrier.","scan","AI took down the language barrier. You're the people in this room, and the mundane work is what AI is for."),
}

D[9]=('The goal','scan','The goal: build a bridge from AI skeptic to AI native, together, in a meaningful way. Skeptical users, a nervous team, gung-ho leaders and a racing market all cross the same bridge, in plain language, with nobody gatekept out. Worries get heard, not dismissed, and the human stays in charge.')
D[13]=('Hype is a glass ceiling','fade',"Technical talk, and hype, can make people feel they don't have the expertise to question it, which builds another glass ceiling. Product teams run a handful of very specific agents on a build, not a swarm. The plain question anyone can ask: what problem are you solving?")
D[18]=('Play: Out of the box LLM','pixel',"Play was about individual AI use: find a way to make your own work better. It's about psychological safety and giving people time to learn within the bounds of work. I gave the team access to AI tools and one goal: find new ways to use AI. Low risk, low pressure, internal only.")
D[19]=('How we played','fade',D[19][2])
D[23]=('Results: mundane to strategic','scan',D[23][2])
D[26]=('Search: an answer, not a chat','fade',"We watched users click through each product on the dashboard and fail to find things. We deliberately skipped an open-ended chatbot or agent. Instead we made search smart: based on what someone searched, we could solve the problem or serve the right content, an answer instead of a conversation. Customer sentiment held steady while product adoption rose.")
D[27]=('Keep an eye on AI. Fix the source.','fade',D[27][2])
D[38]=('Feedback tool: walkthrough','fade','Video walkthrough of the feedback tool. It pulls from community posts, support tickets, surveys and more, classifies them with AI, and shows a dashboard. Months of research became minutes.')
D[39]=('Content scorer: walkthrough','fade',"Video walkthrough of the content scorer. It scores customer-facing words against the style rules, and one product area's average score rose by about a third.")
D[40]=('Papercut report: walkthrough','fade','Video walkthrough of the papercut report. It finds small usability problems in a systematic way, and led to dozens of improvements in record time.')
D[41]=('Cloudy search: the real screens','fade','Cloudy search, on the real product screens.')
D[42]=('The real tool','fade','Space to show the actual content tool.')
D[43]=('What we learned','pixel',"Section header: what we learned along the way. The slides that follow list each learning.")

D[3]=('The phases of AI adoption','pixel','Three phases to remember: Play (try it), Build (make it), Design (shape it). Around them, like building a real bridge: Before is the survey and permits (concerns and goals). After is opening day (the result and what we learned).')
D[7]=('The market is pushing','fade','The market was racing, and everyone was talking about it in jargon. Keeping up felt mandatory.')
D[12]=('When designers became engineers','blinds','Pitfall in the build phase: designers started acting as engineers, and a team of "I" leads to burnout. We worked together, learned more about development and model training, reached out to experts, and did not try to do it all alone. The team got more technical and more cross-functional.')
D[32]=('A live moment: a prompt builds a site','fade',D[32][2])
D[101]=('What I hope you take away','fade','Three hopes: one idea you can try today, permission to ask the question you think is too basic, and a reason to share your small wins.')
D[102]=('Leadership was excited','pixel','Leaders said this is the way and were excited to move.')
D[103]=('Users were skeptical','fade','Our customers were highly technical and security-minded, so trust was fragile, and early chatbot experiments raised support tickets.')
D[104]=('The team was opposed','fade','On the team, people worried about the environment, made-up answers (hallucinations), brain rot, ethics, and being left behind or replaced.')
D[105]=('Room to say it out loud','pixel','Before we built anything, we left space to talk through the team\'s concerns before building anything. The worries were real, and they got heard, not dismissed.')
D[106]=('Call concerns resistance, and people go quiet','blinds','Pitfall: when concerns are treated as resistance, people stop saying them out loud, and you lose the information you need.')
D[107]=('The team said the hard stuff out loud','scan','The payoff: the team felt safe enough to say the hard stuff, which made every step after this easier.')
D[108]=('Our work showed up in the company\'s goals','scan','The payoff of setting goals that made sense: the team\'s work connected up to the roadmap and company goals, so leadership could see it.')
D[109]=('Some experts kept the keys','blinds','Pitfall: internal experts gatekeeping with more access and more jargon. Everyone else waits outside, which is another glass ceiling.')
D[110]=('Napkin sketch. Yes, and. Real tool.','scan','The payoff of play: ideas that became real tools. "Yes, and" is from improv: accept the idea, then add to it. It is how a napkin sketch becomes a team build.')
D[111]=('The paper napkin: prototype it, then build as a team','fade','How we fixed the build pitfall: the paper napkin. Go run and do fun stuff, test your ideas in a prototype, then throw it away and work as a team. Engineering teams find more stable builds in code and see flaws you cannot. Understand your value in the room and others\' value too.')
D[112]=('More technical. More cross-functional.','scan','The payoff of building: the team got more technical and more cross-functional.')
D[113]=('We knew what could happen','scan','AI often means dropping in a chatbot. Because we understood what AI could do, we designed something much better.')
D[114]=('Ask if code can do it','pixel','Tip: if you keep prompting the same thing, ask AI whether code or a script could do it for you today.')
D[115]=('Start a folder. Save things.','fade','Tip: collect ideas, tools and patterns in a folder you can reuse. Designing with AI is a lot about curation. I saved an open-source slide repo to a library for this very project.')
D[116]=('Nothing is impossible anymore','fade','Tip: assume it can be done, then ask.')
D[117]=('Think of one person you are solving for','fade','Tip: think about how AI could make the world better for the person you are problem solving for.')
D[118]=('Learn the tools you have','fade','Tip: learn more about the tools we already have access to.')
D[119]=('Share it. Celebrate it.','fade','Tip: share and celebrate openly. Everything is new, and the small things people are already doing are clever solutions.')

D[20]=('Share. Teach. Celebrate. Publish.','fade','Share: biweekly sprint reviews and internal blogs kept everyone in sync, nothing in the shadows. Teach what we did and why, so others reuse the thinking, not just copy the output. Celebrate: quarterly demos let everyone be seen. Publish: documentation, guidance and external blogs, so sharing and celebrating reached our customers too.')
D[119]=('Share it. Celebrate it.','fade','Tip: share and celebrate openly, with customers too: publish documentation and guidance, post internal blogs, post external blogs. Everything is new, and the small things people are already doing are clever solutions.')

D[120]=('The first pancake sucks','blinds','Tip: the first time you build a prompt or tool, it is not going to be great. You will tweak, edit and nudge, and that takes time and can be frustrating. Once one works, you have solved a future-you problem, and your next tool will be better because you know what went wrong the first time.')

D[9]=(D[9][0],D[9][1],D[9][2]+' '+D[8][2])
D[119]=(D[119][0],D[119][1],D[119][2]+' Also: learn more about the tools you already have access to. '+D[118][2])
D[20]=('Share. Teach. Celebrate. Publish.','fade','Share: biweekly reviews and internal blogs kept everyone in sync. Teach what we did and why. Celebrate with quarterly demos. Publish docs, guidance and external blogs, so sharing and celebrating reached customers too.')
D[110]=('A napkin idea became a real tool','scan','Someone sketched an idea on a napkin. We said "Yes, and" (accept the idea, then add to it) and built on it instead of shutting it down. That is how play turned into real tools.')
D[18]=('Play: Out of the box LLM','pixel',"Play was tied to the goals, but the goal was broad to start. It was about finding ways to improve your own workflow, not other people's. That lowered the risk and gave people space to just try things out. It's about psychological safety, not a set-aside block of time.")
D[7]=('The market is pushing','fade','The market was (and still is) racing, and everyone was talking about it in jargon. Keeping up felt mandatory.')
D[102]=('Leadership was excited','pixel','Leaders said this is the way and were excited to move. Quote on the slide, from our CEO: "If you think your job is to argue for manual screwdrivers, you\'re not going to have fun over the next 20 years."')
D[105]=('Room to say it out loud','pixel',"Before we built anything, we left space to talk through the team's concerns. The worries were real (the environment, made-up answers, brain rot, ethics, data, accountability, craft, being replaced), and they got heard, not dismissed. Being replaced was the one I addressed right away.")
D[116]=('Nothing is impossible anymore','fade','Tip: nothing is impossible anymore. The old reasons (we cannot build that, it needs an engineering quarter, it is not our job) are worth asking about again. Ask anyway.')
D[109]=('Experts who keep the keys','blinds','Pitfall to watch for: internal experts gatekeeping with more access and more jargon. Everyone else waits outside, which is another glass ceiling.')

D[104]=('The team was concerned','fade','On the team, people were concerned about the environment, made-up answers (hallucinations), brain rot, ethics, and being left behind or replaced.')
D[102]=(D[102][0],D[102][1],'Leaders said this is the way and were excited to move. Quote on the slide, from the CEO: "If you think your job is to argue for manual screwdrivers, you\'re not going to have fun over the next 20 years."')
D[7]=(D[7][0],D[7][1],D[7][2]+' Hype note: technical talk can make people feel they are not allowed to question it, which builds another glass ceiling. The plain question anyone can ask: what problem are you solving? '+D[13][2])

D[121]=('Three experiences','blinds','')
D[122]=('Inline insights: help right where you work','fade','')
D[32]=('Go tinker','fade',D[32][2])

D[41]=('Cloudy search: the real screens','fade','Cloudy search, on the real product screens.')

D[42]=('The real tool: Cloudy monitoring','fade',D[42][2])

D[123]=('Papercut report: how it works','fade','')
D[124]=('From feedback to fixes','fade','')

D[40]=('Papercut report: how it works','fade','')
D[125]=('Chunkability: the stranger test','fade','')

D[41]=('Cloudy search: dashboard walkthrough','fade',D[41][2])
D[42]=('Prompt monitoring: so we knew what was happening','fade',D[42][2])
D[125]=('Chunkability: keeping the agent in line','fade',D[125][2])
D[27]=('Hype over the customer','blinds',D[27][2])
