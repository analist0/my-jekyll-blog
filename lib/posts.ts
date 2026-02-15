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

function toStringArray(value: unknown): string[] {
  if (value == null) return []
  if (Array.isArray(value)) {
    const result: string[] = []
    for (let i = 0; i < value.length; i++) {
      const nested = toStringArray(value[i])
      for (let j = 0; j < nested.length; j++) {
        result.push(nested[j])
      }
    }
    return result
  }
  const str = String(value).trim()
  if (str === "") return []
  if (str.includes(",")) {
    return str.split(",").map((s) => s.trim()).filter(Boolean)
  }
  return str.split(/\s+/).filter(Boolean)
}

function parseSinglePost(fileName: string): PostMeta {
  const slug = fileName.replace(/\.md$/, "")
  const fullPath = path.join(postsDirectory, fileName)
  const fileContents = fs.readFileSync(fullPath, "utf8")
  const { data, content } = matter(fileContents)

  const plainText = content
    .replace(/[#*`\[\]()!>\-|]/g, "")
    .replace(/\n+/g, " ")
    .trim()
  const excerpt =
    plainText.substring(0, 200) + (plainText.length > 200 ? "..." : "")

  const cats = toStringArray(data.categories) 
  const fallbackCats = cats.length > 0 ? cats : toStringArray(data.category)
  const tags = toStringArray(data.tags)

  return {
    slug,
    title: data.title || slug.replace(/-/g, " "),
    date: data.date
      ? new Date(data.date).toISOString()
      : new Date().toISOString(),
    categories: fallbackCats,
    tags,
    excerpt,
    author: data.author || "analist0",
  }
}

export function getAllPosts(): PostMeta[] {
  if (!fs.existsSync(postsDirectory)) return []

  const fileNames = fs.readdirSync(postsDirectory)
  const allPosts: PostMeta[] = []

  for (const fileName of fileNames) {
    if (!fileName.endsWith(".md")) continue
    try {
      allPosts.push(parseSinglePost(fileName))
    } catch {
      // Skip malformed posts
    }
  }

  allPosts.sort(
    (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()
  )
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
  const excerpt =
    plainText.substring(0, 200) + (plainText.length > 200 ? "..." : "")

  const cats = toStringArray(data.categories)
  const fallbackCats = cats.length > 0 ? cats : toStringArray(data.category)
  const tags = toStringArray(data.tags)

  return {
    slug,
    title: data.title || slug.replace(/-/g, " "),
    date: data.date
      ? new Date(data.date).toISOString()
      : new Date().toISOString(),
    categories: fallbackCats,
    tags,
    excerpt,
    author: data.author || "analist0",
    contentHtml,
  }
}
