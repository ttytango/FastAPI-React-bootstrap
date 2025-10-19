import { atom } from 'recoil'

export type ToastVariant = 'success' | 'error' | 'warning' | 'info'

export type Toast = {
  id: string
  title: string
  message?: string
  variant: ToastVariant
}

export const toastsState = atom<Toast[]>({
  key: 'toastsState',
  default: [],
})



