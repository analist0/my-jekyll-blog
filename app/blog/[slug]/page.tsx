import type { Metadata } from "next"
import Link from "next/link"
import { notFound } from "next/navigation"
import { getAllPosts, getPostBySlug, formatDate } from "@/lib/posts"
import { ArrowRight, ArrowLeft, Clock, User } from "lucide-react"

export function generateStaticParams() {
  const posts = getAllPosts()
  return posts.map((post) => ({ slug: post.slug }))
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>
}): Promise<Metadata> {
  const { slug } = await params
  const post = await getPostBySlug(slug)
  if (!post) return { title: "Not Found" }
  return {
    title: post.title,
    description: post.excerpt,
  }
}

export default async function BlogPostPage({
  params,
}: {
  params: Promise<{ slug: string }>
}) {
  const { slug } = await params
  const post = await getPostBySlug(slug)
  if (!post) notFound()

  const allPosts = getAllPosts()
  const currentIndex = allPosts.findIndex((p) => p.slug === slug)
  const prevPost = currentIndex < allPosts.length - 1 ? allPosts[currentIndex + 1] : null
  const nextPost = currentIndex > 0 ? allPosts[currentIndex - 1] : null

  const wordCount = post.contentHtml.replace(/<[^>]+>/g, "").split(/\s+/).length
  const readingTime = Math.max(1, Math.round(wordCount / 200))

  return (
    <article className="mx-auto max-w-3xl px-4 pb-20 pt-10">
      {/* Breadcrumb */}
      <nav className="mb-8 flex items-center gap-2 text-xs text-muted-foreground" aria-label="Breadcrumb">
        <Link href="/" className="transition-colors hover:text-foreground">
          בית
        </Link>
        <span>/</span>
        <Link href="/blog" className="transition-colors hover:text-foreground">
          בלוג
        </Link>
        <span>/</span>
        <span className="truncate text-foreground">{post.title}</span>
      </nav>

      {/* Header */}
      <header className="mb-10">
        {post.categories.length > 0 && (
          <span className="mb-3 inline-flex rounded-full bg-primary/10 px-3 py-1 text-xs font-medium text-primary">
            {post.categories[0]}
          </span>
        )}
        <h1 className="text-balance text-3xl font-bold leading-tight text-foreground md:text-4xl">
          {post.title}
        </h1>
        <div className="mt-4 flex flex-wrap items-center gap-4 text-xs text-muted-foreground">
          <span className="flex items-center gap-1.5">
            <User className="h-3.5 w-3.5" />
            {post.author}
          </span>
          <time className="flex items-center gap-1.5" dateTime={post.date}>
            {formatDate(post.date)}
          </time>
          <span className="flex items-center gap-1.5">
            <Clock className="h-3.5 w-3.5" />
            {readingTime} {"min read"}
          </span>
        </div>
        {post.tags.length > 0 && (
          <div className="mt-4 flex flex-wrap gap-1.5">
            {post.tags.map((tag) => (
              <span
                key={tag}
                className="rounded-md bg-muted px-2 py-0.5 text-[10px] font-medium text-muted-foreground"
              >
                #{tag}
              </span>
            ))}
          </div>
        )}
      </header>

      {/* Content */}
      <div
        className="prose prose-sm prose-invert max-w-none"
        dangerouslySetInnerHTML={{ __html: post.contentHtml }}
      />

      {/* Share */}
      <div className="mt-16 border-t border-border pt-8">
        <p className="mb-4 text-sm font-medium text-foreground">Share this article</p>
        <div className="flex flex-wrap gap-2">
          <a
            href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(post.title)}&url=${encodeURIComponent(`https://analist0.github.io/my-jekyll-blog/blog/${slug}`)}`}
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-lg border border-border bg-card px-4 py-2 text-xs font-medium text-foreground transition-colors hover:bg-muted"
          >
            Twitter / X
          </a>
          <a
            href={`https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(`https://analist0.github.io/my-jekyll-blog/blog/${slug}`)}&title=${encodeURIComponent(post.title)}`}
            target="_blank"
            rel="noopener noreferrer"
            className="rounded-lg border border-border bg-card px-4 py-2 text-xs font-medium text-foreground transition-colors hover:bg-muted"
          >
            LinkedIn
          </a>
        </div>
      </div>

      {/* Navigation */}
      <nav className="mt-10 grid gap-4 md:grid-cols-2" aria-label="Post navigation">
        {prevPost ? (
          <Link
            href={`/blog/${prevPost.slug}`}
            className="group flex flex-col rounded-xl border border-border bg-card p-4 transition-all hover:border-primary/30"
          >
            <span className="mb-1 flex items-center gap-1 text-[10px] text-muted-foreground">
              <ArrowRight className="h-3 w-3" />
              הקודם
            </span>
            <span className="line-clamp-2 text-sm font-medium text-foreground transition-colors group-hover:text-primary">
              {prevPost.title}
            </span>
          </Link>
        ) : (
          <div />
        )}
        {nextPost ? (
          <Link
            href={`/blog/${nextPost.slug}`}
            className="group flex flex-col items-end rounded-xl border border-border bg-card p-4 text-left transition-all hover:border-primary/30"
          >
            <span className="mb-1 flex items-center gap-1 text-[10px] text-muted-foreground">
              הבא
              <ArrowLeft className="h-3 w-3" />
            </span>
            <span className="line-clamp-2 text-sm font-medium text-foreground transition-colors group-hover:text-primary">
              {nextPost.title}
            </span>
          </Link>
        ) : (
          <div />
        )}
      </nav>
    </article>
  )
}
