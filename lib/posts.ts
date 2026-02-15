import "server-only"
import fs from "fs"
import path from "path"
import matter from "gray-matter"
import { remark } from "remark"
import html from "remark-html"
import type { PostMeta, Post } from "./posts-utils"

export type { PostMeta, Post }
export { formatDate, getReadingTime } from "./posts-utils"

const postsDirectory = path.join(process.cwd(), "_posts")

function normalizeList(value: unknown): string[] {
  if (!value) return []
  if (Array.isArray(value)) return value.map(String)
  if (typeof value === "string") return value.split(",").map((s) => s.trim()).filter(Boolean)
  return []
}

export function getAllPosts(): PostMeta[] {
  if (!fs.existsSync(postsDirectory)) return []

  const fileNames = fs.readdirSync(postsDirectory)
  const allPosts = fileNames
    .filter((name) => name.endsWith(".md"))
    .map((fileName) => {
      const slug = fileName.replace(/\.md$/, "")
      const fullPath = path.join(postsDirectory, fileName)
      const fileContents = fs.readFileSync(fullPath, "utf8")
      const { data, content } = matter(fileContents)

      const plainText = content
        .replace(/[#*`\[\]()!>\-|]/g, "")
        .replace(/\n+/g, " ")
        .trim()
      const excerpt = plainText.substring(0, 200) + (plainText.length > 200 ? "..." : "")

      return {
        slug,
        title: data.title || slug.replace(/-/g, " "),
        date: data.date ? new Date(data.date).toISOString() : new Date().toISOString(),
        categories: normalizeList(data.categories || data.category),
        tags: normalizeList(data.tags),
        excerpt,
        author: data.author || "analist0",
      }
    })

  allPosts.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
  return allPosts
}

export async function getPostBySlug(slug: string): Promise<Post | null> {
  if (!fs.existsSync(postsDirectory)) return null

  const fullPath = path.join(postsDirectory, `${slug}.md`)
  if (!fs.existsSync(fullPath)) return null

  const fileContents = fs.readFileSync(fullPath, "utf8")
  const { data, content } = matter(fileContents)

  const processed = await remark().use(html).process(content)
  const contentHtml = processed.toString()

  const plainText = content
    .replace(/[#*`\[\]()!>\-|]/g, "")
    .replace(/\n+/g, " ")
    .trim()
  const excerpt = plainText.substring(0, 200) + (plainText.length > 200 ? "..." : "")

  return {
    slug,
    title: data.title || slug.replace(/-/g, " "),
    date: data.date ? new Date(data.date).toISOString() : new Date().toISOString(),
    categories: normalizeList(data.categories || data.category),
    tags: normalizeList(data.tags),
    excerpt,
    author: data.author || "analist0",
    contentHtml,
  }
}

export function getUniqueCategories(): string[] {
  const posts = getAllPosts()
  const categories = new Set<string>()
  posts.forEach((post) => {
    post.categories.forEach((cat) => categories.add(cat))
  })
  return Array.from(categories)
}


