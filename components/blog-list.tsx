"use client"

import { useState, useMemo } from "react"
import Link from "next/link"
import { formatDate, type PostMeta } from "@/lib/posts-utils"
import { Search } from "lucide-react"
import { cn } from "@/lib/utils"

const POSTS_PER_PAGE = 20

export function BlogList({
  posts,
  categories,
}: {
  posts: PostMeta[]
  categories: string[]
}) {
  const [search, setSearch] = useState("")
  const [activeCategory, setActiveCategory] = useState<string | null>(null)
  const [page, setPage] = useState(1)

  const filtered = useMemo(() => {
    let result = posts
    if (search) {
      const q = search.toLowerCase()
      result = result.filter(
        (p) =>
          p.title.toLowerCase().includes(q) ||
          p.excerpt.toLowerCase().includes(q) ||
          p.tags.some((t) => t.toLowerCase().includes(q))
      )
    }
    if (activeCategory) {
      result = result.filter((p) => p.categories.includes(activeCategory))
    }
    return result
  }, [posts, search, activeCategory])

  const paginated = filtered.slice(0, page * POSTS_PER_PAGE)
  const hasMore = paginated.length < filtered.length

  return (
    <div className="flex flex-col gap-8">
      {/* Search & Filters */}
      <div className="flex flex-col gap-4 md:flex-row md:items-center md:gap-6">
        <div className="relative flex-1">
          <Search className="absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
          <input
            type="text"
            placeholder="חיפוש פוסטים..."
            value={search}
            onChange={(e) => {
              setSearch(e.target.value)
              setPage(1)
            }}
            className="w-full rounded-lg border border-border bg-card py-2.5 pe-4 ps-10 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary"
          />
        </div>

        <div className="flex flex-wrap gap-1.5">
          <button
            onClick={() => {
              setActiveCategory(null)
              setPage(1)
            }}
            className={cn(
              "rounded-md px-3 py-1.5 text-xs font-medium transition-colors",
              !activeCategory
                ? "bg-primary text-primary-foreground"
                : "bg-muted text-muted-foreground hover:bg-muted/80"
            )}
          >
            הכל
          </button>
          {categories.slice(0, 8).map((cat) => (
            <button
              key={cat}
              onClick={() => {
                setActiveCategory(cat === activeCategory ? null : cat)
                setPage(1)
              }}
              className={cn(
                "rounded-md px-3 py-1.5 text-xs font-medium transition-colors",
                activeCategory === cat
                  ? "bg-primary text-primary-foreground"
                  : "bg-muted text-muted-foreground hover:bg-muted/80"
              )}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {/* Results count */}
      <p className="text-xs text-muted-foreground">
        {filtered.length} {filtered.length === 1 ? "פוסט" : "פוסטים"}
      </p>

      {/* Posts */}
      <div className="flex flex-col divide-y divide-border">
        {paginated.map((post) => (
          <Link
            key={post.slug}
            href={`/blog/${post.slug}`}
            className="group flex flex-col gap-1 py-5 transition-colors hover:bg-muted/30 md:flex-row md:items-start md:gap-8 md:rounded-lg md:px-4"
          >
            <time className="shrink-0 text-xs tabular-nums text-muted-foreground md:w-28 md:pt-0.5">
              {formatDate(post.date)}
            </time>
            <div className="flex-1">
              <h3 className="line-clamp-2 text-sm font-semibold text-foreground transition-colors group-hover:text-primary">
                {post.title}
              </h3>
              <p className="mt-1 line-clamp-2 text-xs leading-relaxed text-muted-foreground">
                {post.excerpt}
              </p>
              {post.tags.length > 0 && (
                <div className="mt-2 flex flex-wrap gap-1">
                  {post.tags.slice(0, 3).map((tag) => (
                    <span
                      key={tag}
                      className="rounded bg-muted px-1.5 py-0.5 text-[10px] text-muted-foreground"
                    >
                      #{tag}
                    </span>
                  ))}
                </div>
              )}
            </div>
            {post.categories.length > 0 && (
              <span className="mt-2 inline-flex w-fit shrink-0 rounded-full bg-muted px-2.5 py-0.5 text-[10px] font-medium text-muted-foreground md:mt-0">
                {post.categories[0]}
              </span>
            )}
          </Link>
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="py-20 text-center">
          <p className="text-sm text-muted-foreground">
            לא נמצאו פוסטים.
          </p>
        </div>
      )}

      {hasMore && (
        <button
          onClick={() => setPage((p) => p + 1)}
          className="mx-auto rounded-lg border border-border bg-card px-6 py-2.5 text-sm font-medium text-foreground transition-colors hover:bg-muted"
        >
          טען עוד
        </button>
      )}
    </div>
  )
}
