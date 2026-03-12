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
