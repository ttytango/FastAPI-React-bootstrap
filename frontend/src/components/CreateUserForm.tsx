import { useState } from 'react'
import { createUser } from '../api/auth'
import { useToast } from '../hooks/useToast'
import Button from './ui/Button'

export default function CreateUserForm() {
  const toast = useToast()
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError('')
    try {
      await createUser({ username, email, password, role: 'user' })
      toast.success('Success', 'User created. Now login.')
    } catch (err: any) {
      setError(err.message.detail ?? 'Failed to create user')
      toast.error('Failed to create user', err.message.detail)
    }
  }

  return (
    <section>
      <h2 className="text-lg font-semibold mb-4">1) Create User</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Username</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" value={username} onChange={e => setUsername(e.target.value)} required minLength={3} maxLength={50} />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Email</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" type="email" value={email} onChange={e => setEmail(e.target.value)} required />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Password</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" type="password" value={password} onChange={e => setPassword(e.target.value)} required minLength={8} maxLength={128} />
        </div>
        <Button type="submit">Create</Button>
      </form>
      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
    </section>
  )
}


