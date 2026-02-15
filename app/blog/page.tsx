import type { Metadata } from "next"
import { getAllPosts } from "@/lib/posts"
import { BlogList } from "@/components/blog-list"

export const metadata: Metadata = {
  title: "Blog",
  description: "Technical articles, guides, and deep dives on AI, security, development and more.",
}

export default function BlogPage() {
  const posts = getAllPosts()
  const categories = Array.from(
    new Set(posts.flatMap((post) => (Array.isArray(post.categories) ? post.categories : [])))
  )

  return (
    <div className="mx-auto max-w-6xl px-4 pb-20 pt-10">
      <div className="mb-10">
        <p className="text-xs font-medium uppercase tracking-widest text-primary">
          בלוג
        </p>
        <h1 className="mt-1 text-3xl font-bold text-foreground">כל הפוסטים</h1>
        <p className="mt-2 text-sm text-muted-foreground">
          מאמרים, מדריכים וכתבות טכנולוגיות מעמיקות
        </p>
      </div>

      <BlogList posts={posts} categories={categories} />
    </div>
  )
}
