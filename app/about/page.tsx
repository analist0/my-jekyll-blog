import type { Metadata } from "next"
import Link from "next/link"
import { Code2, Cpu, Shield, Workflow, Mail, Github, Linkedin, Twitter } from "lucide-react"

export const metadata: Metadata = {
  title: "About",
  description: "About analist0 - Full-Stack Developer, UI/UX Designer & Tech Enthusiast.",
}

const techStack = [
  { category: "Languages", items: ["Python", "JavaScript", "TypeScript", "Go", "Bash", "Rust"] },
  { category: "Frontend", items: ["React", "Next.js", "TailwindCSS", "HTML/CSS"] },
  { category: "Backend", items: ["Node.js", "Express", "FastAPI", "Django"] },
  { category: "AI/ML", items: ["Ollama", "LangChain", "Hugging Face", "OpenAI API"] },
  { category: "DevOps", items: ["Docker", "GitHub Actions", "Nginx", "Linux"] },
  { category: "Tools", items: ["Git", "n8n", "Termux", "VS Code", "Neovim"] },
]

const socialLinks = [
  { icon: Github, label: "GitHub", href: "https://github.com/analist0" },
  { icon: Twitter, label: "Twitter", href: "https://twitter.com/analist0" },
  { icon: Linkedin, label: "LinkedIn", href: "https://linkedin.com/in/analist0" },
  { icon: Mail, label: "Email", href: "mailto:contact@example.com" },
]

export default function AboutPage() {
  return (
    <div className="mx-auto max-w-3xl px-4 pb-20 pt-10">
      <div className="mb-12">
        <p className="text-xs font-medium uppercase tracking-widest text-primary">
          אודות
        </p>
        <h1 className="mt-1 text-3xl font-bold text-foreground">יוסי</h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Full-Stack Developer & Tech Enthusiast
        </p>
      </div>

      {/* Bio */}
      <div className="mb-12 flex flex-col gap-4 text-sm leading-relaxed text-muted-foreground">
        <p>
          אני מפתח תוכנה עם ניסיון של מספר שנים בפיתוח Full-Stack, אוטומציה ו-DevOps.
          מתמחה בבניית כלים מתקדמים, סוכני AI, ומערכות אוטומציה.
        </p>
        <p>
          התשוקה שלי היא ללמוד ולחקור טכנולוגיות חדשות, ולשתף את הידע עם הקהילה
          דרך מדריכים מעמיקים, פרויקטים בקוד פתוח, ופוסטים טכניים.
        </p>
        <p>
          כשאני לא כותב קוד, אני כנראה מנסה כלי AI חדש, בונה אוטומציה מורכבת,
          או מנסה להריץ מודל שפה מקומי על החומרה שלי.
        </p>
      </div>

      {/* Expertise areas */}
      <div className="mb-12">
        <h2 className="mb-6 text-lg font-bold text-foreground">תחומי התמחות</h2>
        <div className="grid grid-cols-2 gap-3">
          {[
            { icon: Code2, label: "Full-Stack Development", desc: "React, Node.js, Python" },
            { icon: Cpu, label: "AI & Machine Learning", desc: "LLMs, Agents, Local AI" },
            { icon: Shield, label: "Security & DevSecOps", desc: "Penetration Testing, Hardening" },
            { icon: Workflow, label: "Automation & DevOps", desc: "n8n, Docker, CI/CD" },
          ].map((area) => (
            <div
              key={area.label}
              className="flex flex-col gap-2 rounded-xl border border-border bg-card p-4"
            >
              <area.icon className="h-5 w-5 text-primary" />
              <h3 className="text-xs font-semibold text-foreground">{area.label}</h3>
              <p className="text-[11px] text-muted-foreground">{area.desc}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Tech Stack */}
      <div className="mb-12">
        <h2 className="mb-6 text-lg font-bold text-foreground">Tech Stack</h2>
        <div className="flex flex-col gap-4">
          {techStack.map((group) => (
            <div key={group.category} className="flex flex-col gap-2 md:flex-row md:items-start md:gap-6">
              <span className="w-24 shrink-0 text-xs font-semibold text-foreground">
                {group.category}
              </span>
              <div className="flex flex-wrap gap-1.5">
                {group.items.map((item) => (
                  <span
                    key={item}
                    className="rounded-md border border-border bg-card px-2.5 py-1 text-xs text-muted-foreground"
                  >
                    {item}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Social */}
      <div>
        <h2 className="mb-6 text-lg font-bold text-foreground">Contact</h2>
        <div className="flex flex-wrap gap-3">
          {socialLinks.map((link) => (
            <Link
              key={link.label}
              href={link.href}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 rounded-lg border border-border bg-card px-4 py-2.5 text-sm text-foreground transition-colors hover:border-primary/30 hover:text-primary"
            >
              <link.icon className="h-4 w-4" />
              {link.label}
            </Link>
          ))}
        </div>
      </div>
    </div>
  )
}
