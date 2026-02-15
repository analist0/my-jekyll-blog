import Link from "next/link"
import { getAllPosts, formatDate } from "@/lib/posts"
import { ArrowLeft, Code2, Cpu, Shield, Workflow } from "lucide-react"

const projects = [
  {
    title: "MCP Servers Collection",
    description: "16 MCP Servers with backup, file uploads, databases and more.",
    tags: ["Python", "Node.js", "API"],
    href: "https://github.com/analist0/claude-code-config",
  },
  {
    title: "AI News Aggregator",
    description: "Automated n8n workflow collecting AI news from 13 sources.",
    tags: ["n8n", "RSS", "Telegram"],
    href: "#",
  },
  {
    title: "Claude Agent System",
    description: "Autonomous AI agent with Ollama, full memory, and task tracking.",
    tags: ["Python", "Ollama", "LLM"],
    href: "#",
  },
]

const skills = [
  { icon: Code2, label: "Full-Stack", desc: "Python, JavaScript, Node.js, React" },
  { icon: Cpu, label: "AI & ML", desc: "Ollama, LLMs, Agents, Automation" },
  { icon: Shield, label: "Security", desc: "Penetration Testing, DevSecOps" },
  { icon: Workflow, label: "DevOps", desc: "Docker, CI/CD, Cloud, n8n" },
]

export default function HomePage() {
  const posts = getAllPosts().slice(0, 4)

  return (
    <div className="flex flex-col">
      {/* Hero */}
      <section className="relative flex items-center justify-center overflow-hidden px-4 pb-20 pt-32">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,hsl(168_76%_42%_/_0.08),transparent_60%)]" />
        <div className="relative mx-auto max-w-3xl text-center">
          <p className="mb-4 text-sm font-medium tracking-wider text-primary">
            Full-Stack Developer
          </p>
          <h1 className="text-balance text-4xl font-bold leading-tight tracking-tight text-foreground md:text-6xl">
            בונה כלים מתקדמים.
            <br />
            <span className="text-primary">משתף ידע.</span>
          </h1>
          <p className="mx-auto mt-6 max-w-xl text-pretty text-lg leading-relaxed text-muted-foreground">
            מפתח Full-Stack עם התמחות ב-AI, אוטומציה ואבטחת מידע. יוצר תוכן טכנולוגי, מדריכים
            מעמיקים ופרויקטים בקוד פתוח.
          </p>
          <div className="mt-8 flex flex-wrap items-center justify-center gap-3">
            <Link
              href="/portfolio"
              className="inline-flex items-center gap-2 rounded-lg bg-primary px-5 py-2.5 text-sm font-semibold text-primary-foreground transition-colors hover:bg-primary/90"
            >
              הפרויקטים שלי
              <ArrowLeft className="h-4 w-4" />
            </Link>
            <Link
              href="/blog"
              className="inline-flex items-center gap-2 rounded-lg border border-border bg-card px-5 py-2.5 text-sm font-semibold text-foreground transition-colors hover:bg-muted"
            >
              הבלוג
            </Link>
          </div>
        </div>
      </section>

      {/* Skills */}
      <section className="border-y border-border bg-card/50 px-4 py-16">
        <div className="mx-auto max-w-6xl">
          <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
            {skills.map((skill) => (
              <div
                key={skill.label}
                className="flex flex-col items-center gap-3 rounded-xl border border-border bg-card p-6 text-center transition-colors hover:border-primary/30"
              >
                <skill.icon className="h-6 w-6 text-primary" />
                <h3 className="text-sm font-semibold text-foreground">{skill.label}</h3>
                <p className="text-xs leading-relaxed text-muted-foreground">{skill.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Latest Posts */}
      <section className="px-4 py-20">
        <div className="mx-auto max-w-6xl">
          <div className="mb-10 flex items-end justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest text-primary">
                כתיבה
              </p>
              <h2 className="mt-1 text-2xl font-bold text-foreground">פוסטים אחרונים</h2>
            </div>
            <Link
              href="/blog"
              className="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
            >
              כל הפוסטים
            </Link>
          </div>

          <div className="flex flex-col divide-y divide-border">
            {posts.map((post) => (
              <Link
                key={post.slug}
                href={`/blog/${post.slug}`}
                className="group flex flex-col gap-1 py-5 transition-colors hover:bg-muted/30 md:flex-row md:items-center md:gap-8 md:rounded-lg md:px-4"
              >
                <time className="shrink-0 text-xs tabular-nums text-muted-foreground md:w-32">
                  {formatDate(post.date)}
                </time>
                <div className="flex-1">
                  <h3 className="line-clamp-2 text-sm font-semibold text-foreground transition-colors group-hover:text-primary">
                    {post.title}
                  </h3>
                  <p className="mt-1 line-clamp-2 text-xs leading-relaxed text-muted-foreground">
                    {post.excerpt}
                  </p>
                </div>
                {post.categories.length > 0 && (
                  <span className="mt-2 inline-flex w-fit shrink-0 rounded-full bg-muted px-2.5 py-0.5 text-[10px] font-medium text-muted-foreground md:mt-0">
                    {post.categories[0]}
                  </span>
                )}
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Projects */}
      <section className="border-t border-border bg-card/50 px-4 py-20">
        <div className="mx-auto max-w-6xl">
          <div className="mb-10 flex items-end justify-between">
            <div>
              <p className="text-xs font-medium uppercase tracking-widest text-primary">
                פרויקטים
              </p>
              <h2 className="mt-1 text-2xl font-bold text-foreground">עבודות נבחרות</h2>
            </div>
            <Link
              href="/portfolio"
              className="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
            >
              כל הפרויקטים
            </Link>
          </div>

          <div className="grid gap-4 md:grid-cols-3">
            {projects.map((project) => (
              <Link
                key={project.title}
                href={project.href}
                target={project.href.startsWith("http") ? "_blank" : undefined}
                rel={project.href.startsWith("http") ? "noopener noreferrer" : undefined}
                className="group rounded-xl border border-border bg-card p-6 transition-all hover:border-primary/30 hover:shadow-lg hover:shadow-primary/5"
              >
                <h3 className="text-base font-semibold text-foreground transition-colors group-hover:text-primary">
                  {project.title}
                </h3>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
                  {project.description}
                </p>
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
        </div>
      </section>
    </div>
  )
}
