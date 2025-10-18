import { useState } from 'react'
import { createUser, login, getMe, TokenResponse } from './api/auth'

function App() {
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loginPassword, setLoginPassword] = useState('')
  const [token, setToken] = useState<string>('')
  const [createErr, setCreateErr] = useState<string>('')
  const [loginErr, setLoginErr] = useState<string>('')
  const [me, setMe] = useState<any>(null)

  async function handleCreateUser(e: React.FormEvent) {
    e.preventDefault()
    setCreateErr('')
    try {
      await createUser({ username, email, password, role: 'user' })
      alert('User created. Now login.')
    } catch (err: any) {
      setCreateErr(err.message ?? 'Failed to create user')
    }
  }

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault()
    setLoginErr('')
    try {
      const res: TokenResponse = await login(username, loginPassword)
      setToken(res.access_token)
    } catch (err: any) {
      setLoginErr(err.message ?? 'Login failed')
    }
  }

  async function handleGetMe() {
    try {
      const data = await getMe(token)
      setMe(data)
    } catch (err: any) {
      alert(err.message ?? 'Failed to fetch me')
    }
  }

  return (
    <div style={{ maxWidth: 560, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>Auth Flow</h1>

      <section style={{ padding: '1rem', border: '1px solid #ddd', marginBottom: '1rem' }}>
        <h2>1) Create User</h2>
        <form onSubmit={handleCreateUser}>
          <div>
            <label>Username</label><br />
            <input value={username} onChange={e => setUsername(e.target.value)} required minLength={3} maxLength={50} />
          </div>
          <div>
            <label>Email</label><br />
            <input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
          </div>
          <div>
            <label>Password</label><br />
            <input type="password" value={password} onChange={e => setPassword(e.target.value)} required minLength={8} maxLength={128} />
          </div>
          <button type="submit">Create</button>
        </form>
        {createErr && <p style={{ color: 'red' }}>{createErr}</p>}
      </section>

      <section style={{ padding: '1rem', border: '1px solid #ddd', marginBottom: '1rem' }}>
        <h2>2) Login</h2>
        <form onSubmit={handleLogin}>
          <div>
            <label>Username</label><br />
            <input value={username} onChange={e => setUsername(e.target.value)} required />
          </div>
          <div>
            <label>Password</label><br />
            <input type="password" value={loginPassword} onChange={e => setLoginPassword(e.target.value)} required />
          </div>
          <button type="submit">Get Token</button>
        </form>
        {loginErr && <p style={{ color: 'red' }}>{loginErr}</p>}
        {token && (
          <div>
            <p><strong>Token:</strong> <code style={{wordBreak:'break-all'}}>{token}</code></p>
          </div>
        )}
      </section>

      <section style={{ padding: '1rem', border: '1px solid #ddd' }}>
        <h2>3) Me</h2>
        <button onClick={handleGetMe} disabled={!token}>Fetch Me</button>
        {me && (
          <pre style={{ background:'#f7f7f7', padding:'1rem' }}>{JSON.stringify(me, null, 2)}</pre>
        )}
      </section>
    </div>
  )
}

export default App


