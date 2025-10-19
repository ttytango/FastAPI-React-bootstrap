import { useRecoilState } from 'recoil'
import { toastsState, Toast } from '../state/toast'

const variantStyles: Record<string, string> = {
  success: 'from-emerald-500 to-emerald-700 border-emerald-400',
  error: 'from-rose-500 to-rose-700 border-rose-400',
  warning: 'from-amber-500 to-amber-700 border-amber-400',
  info: 'from-sky-500 to-sky-700 border-sky-400',
}

function ToastItem({ t, onClose }: { t: Toast; onClose: (id: string) => void }) {
  return (
    <div className={`relative rounded-lg border overflow-hidden shadow-lg text-white`}>      
      <div className={`absolute inset-x-0 bottom-0 h-1 bg-gradient-to-r ${variantStyles[t.variant]}`}></div>
      <div className="flex items-center justify-between px-4 py-3 bg-gray-800/90">
        <div className="flex items-start gap-3">
          <div className={`mt-1 h-6 w-6 rounded-full bg-gradient-to-br ${variantStyles[t.variant]} flex items-center justify-center text-white`}>✔</div>
          <div>
            <div className="font-semibold text-lg">{t.title}</div>
            {t.message && <div className="text-sm opacity-90">{t.message}</div>}
          </div>
        </div>
        <button className="text-gray-300 hover:text-white" onClick={() => onClose(t.id)}>✕</button>
      </div>
    </div>
  )
}

export default function ToastContainer() {
  const [toasts, setToasts] = useRecoilState(toastsState)
  const onClose = (id: string) => setToasts(prev => prev.filter(t => t.id !== id))
  return (
    <div className="fixed top-4 right-4 z-50 space-y-3 w-[340px] max-w-[90vw]">
      {toasts.map(t => <ToastItem key={t.id} t={t} onClose={onClose} />)}
    </div>
  )
}



