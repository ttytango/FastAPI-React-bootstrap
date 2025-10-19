import type { ButtonHTMLAttributes, PropsWithChildren } from 'react'

type Props = ButtonHTMLAttributes<HTMLButtonElement> & { className?: string }

export default function Button({ children, className = '', ...props }: PropsWithChildren<Props>) {
  const base =
    'inline-flex items-center justify-center px-4 py-2 rounded-md font-medium text-white ' +
    'bg-blue-600 hover:bg-blue-700 focus-visible:outline-none focus-visible:ring-2 ' +
    'focus-visible:ring-blue-500 focus-visible:ring-offset-2 disabled:opacity-50 ' +
    'transition-colors shadow-sm'

  return (
    <button className={`${base} ${className}`} {...props}>
      {children}
    </button>
  )
}



