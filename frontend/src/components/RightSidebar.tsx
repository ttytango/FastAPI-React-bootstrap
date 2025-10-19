import { useRecoilState, useRecoilValue } from 'recoil'
import { tokenState, isAuthenticatedState } from '../state/auth'

export default function RightSidebar() {
  const [token, setToken] = useRecoilState(tokenState)
  const isAuthed = useRecoilValue(isAuthenticatedState)

  return (
    <aside className="hidden lg:flex lg:flex-col lg:w-64 bg-white border-l border-gray-200 min-h-[calc(100vh-64px)] sticky top-16">
      <div className="p-4 text-sm font-semibold text-gray-500">Session</div>
      <div className="px-4 pb-4 space-y-3">
        <div className="rounded-md border border-gray-200 p-3">
          <div className="text-sm text-gray-600">Authenticated</div>
          <div className={`mt-1 inline-flex items-center gap-2 text-sm font-medium ${isAuthed ? 'text-emerald-600' : 'text-rose-600'}`}>
            <span className={`h-2 w-2 rounded-full ${isAuthed ? 'bg-emerald-500' : 'bg-rose-500'}`}></span>
            {isAuthed ? 'Yes' : 'No'}
          </div>
          {token && (
            <button
              onClick={() => setToken('')}
              className="mt-3 inline-flex items-center justify-center px-3 py-1.5 rounded-md text-white bg-gray-700 hover:bg-gray-800 text-sm"
            >
              Clear Token
            </button>
          )}
        </div>

        <div className="rounded-md border border-gray-200 p-3">
          <div className="text-sm font-semibold mb-2">Quick Links</div>
          <ul className="text-sm text-gray-700 space-y-1">
            <li><a className="hover:underline" href="#">Docs</a></li>
            <li><a className="hover:underline" href="#">Tips</a></li>
            <li><a className="hover:underline" href="#">Changelog</a></li>
          </ul>
        </div>
      </div>
    </aside>
  )
}


