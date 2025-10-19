import { useState } from 'react'
import { useRecoilValue } from 'recoil'
import { getMe } from '../api/auth'
import { tokenState } from '../state/auth'
import { useToast } from '../hooks/useToast'
import Button from './ui/Button'

export default function MePanel() {
  const token = useRecoilValue(tokenState)
  const [me, setMe] = useState<any>(null)
  const toast = useToast()

  async function handleFetch() {
    try {
      const data = await getMe(token)
      setMe(data)
    } catch (err: any) {
      const msg = err?.detail ?? err?.message ?? 'Failed to fetch user information'
      toast.error('Failed', msg)
    }
  }

  return (
    <section>
      <h2 className="text-lg font-semibold mb-4">3) Me</h2>
      <Button onClick={handleFetch} disabled={!token}>Fetch Me</Button>
      {me && (
        <pre className="mt-4 bg-gray-50 p-4 rounded-md">{JSON.stringify(me, null, 2)}</pre>
      )}
    </section>
  )
}


