import fs from "fs"
import path from "path"
import matter from "gray-matter"
import { remark } from "remark"
import html from "remark-html"

const postsDirectory = path.join(process.cwd(), "_posts")

export interface PostMeta {
  slug: string
  title: string
  date: string
  categories: string[]
  tags: string[]
  excerpt: string
  author: string
}

export interface Post extends PostMeta {
  contentHtml: string
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
        categories: data.categories || [],
        tags: data.tags || [],
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
    categories: data.categories || [],
    tags: data.tags || [],
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

export function formatDate(dateString: string): string {
  const date = new Date(dateString)
  return date.toLocaleDateString("he-IL", {
    year: "numeric",
    month: "long",
    day: "numeric",
  })
}

export function getReadingTime(content: string): number {
  const words = content.split(/\s+/).length
  return Math.max(1, Math.round(words / 200))
}
