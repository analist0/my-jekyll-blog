import type { Metadata } from "next"
import Link from "next/link"
import { getAllPosts, formatDate } from "@/lib/posts"
import { BookOpen, Clock } from "lucide-react"

export const metadata: Metadata = {
  title: "Tutorials",
  description: "In-depth technical tutorials on AI, development, security, and more.",
}

const manualTutorials = [
  {
    title: "Build a Blog with Jekyll",
    level: "intermediate" as const,
    duration: "45 min",
    tags: ["Jekyll", "GitHubPages", "RTL"],
  },
  {
    title: "Develop MCP Servers",
    level: "advanced" as const,
    duration: "90 min",
    tags: ["Python", "MCP", "API"],
  },
  {
    title: "Getting Started with Git & GitHub",
    level: "beginner" as const,
    duration: "30 min",
    tags: ["Git", "GitHub", "VersionControl"],
  },
  {
    title: "Automation with n8n",
    level: "intermediate" as const,
    duration: "60 min",
    tags: ["n8n", "Automation", "NoCode"],
  },
  {
    title: "AI Agents with Ollama",
    level: "advanced" as const,
    duration: "120 min",
    tags: ["AI", "Ollama", "LLM"],
  },
  {
    title: "CSS Grid & Flexbox",
    level: "beginner" as const,
    duration: "20 min",
    tags: ["CSS", "Grid", "Flexbox"],
  },
]

const levelColors = {
  beginner: "bg-emerald-500/10 text-emerald-400",
  intermediate: "bg-amber-500/10 text-amber-400",
  advanced: "bg-red-500/10 text-red-400",
}

const levelLabels = {
  beginner: "Beginner",
  intermediate: "Intermediate",
  advanced: "Advanced",
}

export default function TutorialsPage() {
  const tutorialPosts = getAllPosts().filter(
    (p) =>
      p.categories.some((c) => c.toLowerCase().includes("tutorial") || c.toLowerCase().includes("guide")) ||
      p.title.toLowerCase().includes("guide") ||
      p.title.toLowerCase().includes("tutorial") ||
      p.title.toLowerCase().includes("step-by-step") ||
      p.title.toLowerCase().includes("comprehensive")
  ).slice(0, 12)

  return (
    <div className="mx-auto max-w-6xl px-4 pb-20 pt-10">
      <div className="mb-12">
        <p className="text-xs font-medium uppercase tracking-widest text-primary">
          מדריכים
        </p>
        <h1 className="mt-1 text-3xl font-bold text-foreground">מדריכים טכניים</h1>
        <p className="mt-2 max-w-xl text-sm text-muted-foreground">
          מדריכים מעמיקים וייחודיים בנושאים מתקדמים
        </p>
      </div>

      {/* Manual tutorials */}
      <div className="mb-16">
        <h2 className="mb-6 text-lg font-semibold text-foreground">מסלולי למידה</h2>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {manualTutorials.map((tut) => (
            <div
              key={tut.title}
              className="flex flex-col rounded-xl border border-border bg-card p-5 transition-colors hover:border-primary/30"
            >
              <div className="mb-3 flex items-center justify-between">
                <span
                  className={`rounded-full px-2.5 py-0.5 text-[10px] font-semibold ${levelColors[tut.level]}`}
                >
                  {levelLabels[tut.level]}
                </span>
                <span className="flex items-center gap-1 text-xs text-muted-foreground">
                  <Clock className="h-3 w-3" />
                  {tut.duration}
                </span>
              </div>
              <h3 className="mb-2 text-sm font-semibold text-foreground">{tut.title}</h3>
              <div className="mt-auto flex flex-wrap gap-1 pt-3">
                {tut.tags.map((tag) => (
                  <span
                    key={tag}
                    className="rounded bg-muted px-1.5 py-0.5 text-[10px] text-muted-foreground"
                  >
                    #{tag}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Tutorial posts from blog */}
      {tutorialPosts.length > 0 && (
        <div>
          <h2 className="mb-6 flex items-center gap-2 text-lg font-semibold text-foreground">
            <BookOpen className="h-5 w-5 text-primary" />
            מדריכים מהבלוג
          </h2>
          <div className="flex flex-col divide-y divide-border">
            {tutorialPosts.map((post) => (
              <Link
                key={post.slug}
                href={`/blog/${post.slug}`}
                className="group flex flex-col gap-1 py-4 transition-colors hover:bg-muted/30 md:flex-row md:items-center md:gap-6 md:rounded-lg md:px-4"
              >
                <time className="shrink-0 text-xs tabular-nums text-muted-foreground md:w-28">
                  {formatDate(post.date)}
                </time>
                <h3 className="flex-1 line-clamp-2 text-sm font-semibold text-foreground transition-colors group-hover:text-primary">
                  {post.title}
                </h3>
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* Learning paths */}
      <div className="mt-16 grid gap-4 md:grid-cols-3">
        {[
          {
            title: "Beginner",
            items: ["Git & GitHub", "CSS Grid & Flexbox", "Jekyll Basics", "GitHub Pages"],
          },
          {
            title: "Advanced",
            items: ["Jekyll Advanced", "n8n Automation", "MCP Servers", "AI Agents"],
          },
          {
            title: "Integration",
            items: ["API Integration", "Database Design", "Cloud Services", "Full Project"],
          },
        ].map((path) => (
          <div
            key={path.title}
            className="rounded-xl border border-border bg-card p-6"
          >
            <h3 className="mb-4 text-sm font-bold text-foreground">{path.title}</h3>
            <ul className="flex flex-col gap-2">
              {path.items.map((item) => (
                <li
                  key={item}
                  className="flex items-center gap-2 text-xs text-muted-foreground"
                >
                  <span className="h-1 w-1 shrink-0 rounded-full bg-primary" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  )
}
