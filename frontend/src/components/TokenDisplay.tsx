import { useRecoilValue } from 'recoil'
import { tokenState, isAuthenticatedState } from '../state/auth'

export default function TokenDisplay() {
  const token = useRecoilValue(tokenState)
  const isAuthed = useRecoilValue(isAuthenticatedState)
  return (
    <section>
      <h2 className="text-lg font-semibold mb-4">Status</h2>
      <p className="mb-2">{isAuthed ? 'You are authenticated' : 'You are not authenticated'}</p>
      {token && (
        <div>
          <p><strong>Token:</strong> <code className="break-words">{token}</code></p>
        </div>
      )}
    </section>
  )
}


