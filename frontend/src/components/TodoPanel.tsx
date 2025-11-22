import { useState } from 'react'
import { useRecoilValue } from 'recoil'
import { tokenState, isAuthenticatedState } from '../state/auth'
import { useToast } from '../hooks/useToast'
import Button from './ui/Button'
import { createTodo, listTodos, type Todo } from '../api/todos'

export default function TodoPanel() {
  const authed = useRecoilValue(isAuthenticatedState)
  const token = useRecoilValue(tokenState)
  const toast = useToast()
  const [title, setTitle] = useState('')
  const [description, setDescription] = useState('')
  const [todos, setTodos] = useState<Todo[]>([])
  if (!authed) return null

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault()
    try {
      const t = await createTodo(token, { title, description })
      setTodos(prev => [t, ...prev])
      setTitle('')
      setDescription('')
      toast.success('Todo created')
    } catch (err: any) {
      toast.error('Failed to create todo', err?.detail ?? err?.message)
    }
  }

  async function handleRefresh() {
    try {
      const items = await listTodos(token)
      setTodos(items)
    } catch (err: any) {
      toast.error('Failed to load todos', err?.detail ?? err?.message)
    }
  }

  return (
    <section>
      <h2 className="text-lg font-semibold mb-4">4) Todos</h2>
      <form onSubmit={handleCreate} className="space-y-3 mb-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Title</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" value={title} onChange={e=>setTitle(e.target.value)} required />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Description</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" value={description} onChange={e=>setDescription(e.target.value)} />
        </div>
        <Button type="submit" disabled={!token}>Create Todo</Button>
      </form>
      <div className="flex items-center gap-2 mb-2">
        <Button type="button" onClick={handleRefresh} disabled={!token}>Refresh</Button>
      </div>
      <ul className="space-y-2">
        {todos.map(t => (
          <li key={t.id} className="rounded-md border border-gray-200 p-3">
            <div className="font-medium">{t.title}</div>
            {t.description && <div className="text-sm text-gray-600">{t.description}</div>}
          </li>
        ))}
      </ul>
    </section>
  )
}


