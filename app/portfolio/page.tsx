import type { Metadata } from "next"
import Link from "next/link"
import { ExternalLink } from "lucide-react"

export const metadata: Metadata = {
  title: "Portfolio",
  description: "Projects and work by analist0 - Full-Stack Developer.",
}

const projects = [
  {
    title: "Advanced Blog System",
    description:
      "A fully-featured blog with modern design, animations, dark mode, parallax effects, and RTL support. Built with Jekyll and deployed on GitHub Pages.",
    tags: ["Jekyll", "CSS3", "JavaScript"],
    category: "Design",
    href: "https://analist0.github.io/my-jekyll-blog/",
  },
  {
    title: "MCP Servers Collection",
    description:
      "Collection of 16 custom MCP Servers with support for backup, file uploads, databases, and more. Built for Claude Code integration.",
    tags: ["Python", "Node.js", "API"],
    category: "Development",
    href: "https://github.com/analist0/claude-code-config",
  },
  {
    title: "AI News Aggregator",
    description:
      "Automated n8n workflow that aggregates AI news from 13 sources, filters, and sends to Telegram.",
    tags: ["n8n", "RSS", "Telegram"],
    category: "Automation",
    href: "#",
  },
  {
    title: "Claude Agent System",
    description:
      "Autonomous AI agent with Ollama, full memory management, task tracking, and Hebrew interface.",
    tags: ["Python", "Ollama", "LLM"],
    category: "AI",
    href: "#",
  },
  {
    title: "Termux Full Backup",
    description:
      "Complete backup system for Termux environment with compression, encryption, and automatic restore.",
    tags: ["Bash", "Termux", "Android"],
    category: "Tools",
    href: "#",
  },
  {
    title: "Kali-Style Terminal",
    description:
      "Advanced prompt styled like Kali Linux with widgets, RTL support, and tmux status bar.",
    tags: ["Starship", "tmux", "Bash"],
    category: "Design",
    href: "#",
  },
]

export default function PortfolioPage() {
  return (
    <div className="mx-auto max-w-6xl px-4 pb-20 pt-10">
      <div className="mb-12">
        <p className="text-xs font-medium uppercase tracking-widest text-primary">
          פורטפוליו
        </p>
        <h1 className="mt-1 text-3xl font-bold text-foreground">פרויקטים ועבודות</h1>
        <p className="mt-2 max-w-xl text-sm text-muted-foreground">
          פרויקטים שנבנו עם טכנולוגיות מתקדמות -- מ-AI ועד אוטומציה, מאבטחת מידע ועד עיצוב.
        </p>
      </div>

      <div className="grid gap-4 md:grid-cols-2">
        {projects.map((project) => (
          <Link
            key={project.title}
            href={project.href}
            target={project.href.startsWith("http") ? "_blank" : undefined}
            rel={project.href.startsWith("http") ? "noopener noreferrer" : undefined}
            className="group relative flex flex-col justify-between rounded-xl border border-border bg-card p-6 transition-all hover:border-primary/30 hover:shadow-lg hover:shadow-primary/5"
          >
            <div>
              <div className="mb-3 flex items-center justify-between">
                <span className="rounded-full bg-primary/10 px-2.5 py-0.5 text-[10px] font-medium text-primary">
                  {project.category}
                </span>
                {project.href.startsWith("http") && (
                  <ExternalLink className="h-4 w-4 text-muted-foreground opacity-0 transition-opacity group-hover:opacity-100" />
                )}
              </div>

              <h2 className="text-lg font-semibold text-foreground transition-colors group-hover:text-primary">
                {project.title}
              </h2>
              <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                {project.description}
              </p>
            </div>

            <div className="mt-4 flex flex-wrap gap-1.5">
              {project.tags.map((tag) => (
                <span
                  key={tag}
                  className="rounded-md bg-muted px-2 py-0.5 text-[10px] font-medium text-muted-foreground"
                >
                  {tag}
                </span>
              ))}
            </div>
          </Link>
        ))}
      </div>

      {/* CTA */}
      <div className="mt-16 rounded-xl border border-border bg-card p-8 text-center">
        <h2 className="text-xl font-bold text-foreground">רוצים לעבוד ביחד?</h2>
        <p className="mt-2 text-sm text-muted-foreground">
          יש לכם פרויקט מעניין? אשמח לשמוע.
        </p>
        <Link
          href="/about"
          className="mt-4 inline-flex rounded-lg bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90"
        >
          צרו קשר
        </Link>
      </div>
    </div>
  )
}
