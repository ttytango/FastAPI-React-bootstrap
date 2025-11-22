const todoBase = (import.meta as any).env.VITE_TODO_API_URL ?? 'http://localhost:8001';

export type Todo = {
  id: number
  title: string
  description?: string
  completed: boolean
  user_id: number
}

export async function todoApi<T>(path: string, token: string, init: RequestInit = {}): Promise<T> {
  const headers = {
    'Content-Type': 'application/json',
    ...(init.headers || {}),
    Authorization: `Bearer ${token}`,
  } as Record<string, string>
  const res = await fetch(`${todoBase}${path}`, { ...init, headers })
  const ct = res.headers.get('content-type') || ''
  if (!res.ok) {
    try {
      if (ct.includes('application/json')) {
        const data = await res.json()
        throw { status: res.status, detail: data?.detail ?? JSON.stringify(data) }
      }
    } catch {
      // fallthrough
    }
    const text = await res.text().catch(() => '')
    throw { status: res.status, detail: text || res.statusText }
  }
  if (ct.includes('application/json')) return (res.json() as Promise<T>)
  return undefined as unknown as T
}

export function createTodo(
  token: string,
  body: { title: string; description?: string; completed?: boolean }
) {
  return todoApi<Todo>('/todo', token, {
    method: 'POST',
    body: JSON.stringify({ completed: false, ...body }),
  })
}

export function listTodos(token: string) {
  return todoApi<Todo[]>('/todos', token)
}


