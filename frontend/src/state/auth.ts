import { atom, selector } from 'recoil'

export const tokenState = atom<string>({ key: 'tokenState', default: '' })

export const isAuthenticatedState = selector<boolean>({
  key: 'isAuthenticatedState',
  get: ({get}) => !!get(tokenState),
})



