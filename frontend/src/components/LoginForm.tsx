import { useState } from 'react'
import { useSetRecoilState } from 'recoil'
import { login, TokenResponse } from '../api/auth'
import { tokenState } from '../state/auth'
import { useToast } from '../hooks/useToast'
import Button from './ui/Button'

export default function LoginForm() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const setToken = useSetRecoilState(tokenState)
  const toast = useToast()

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    setError('')
    try {
      const res: TokenResponse = await login(username, password)
      setToken(res.access_token)
      toast.success('Logged in', 'Token acquired')
    } catch (err: any) {
      const msg = err?.detail ?? err?.message ?? 'Login failed'
      setError(msg)
      toast.error('Login failed', msg)
    }
  }

  return (
    <section>
      <h2 className="text-lg font-semibold mb-4">2) Login</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700">Username</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" value={username} onChange={e => setUsername(e.target.value)} required />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Password</label>
          <input className="mt-1 w-full rounded-md border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500" type="password" value={password} onChange={e => setPassword(e.target.value)} required />
        </div>
        <Button type="submit">Get Token</Button>
      </form>
      {error && <p className="mt-2 text-sm text-red-600">{error}</p>}
    </section>
  )
}


