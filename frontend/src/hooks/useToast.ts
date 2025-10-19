import { useRecoilCallback } from 'recoil'
import { toastsState, ToastVariant } from '../state/toast'

function uid() {
  return Math.random().toString(36).slice(2)
}

export function useToast() {
  const add = useRecoilCallback(({set}) => (variant: ToastVariant, title: string, message?: string) => {
    const id = uid()
    set(toastsState, (prev) => [...prev, { id, variant, title, message }])
    setTimeout(() => {
      set(toastsState, (prev) => prev.filter(t => t.id !== id))
    }, 4000)
  }, [])

  return {
    success: (title: string, message?: string) => add('success', title, message),
    error: (title: string, message?: string) => add('error', title, message),
    warning: (title: string, message?: string) => add('warning', title, message),
    info: (title: string, message?: string) => add('info', title, message),
  }
}



