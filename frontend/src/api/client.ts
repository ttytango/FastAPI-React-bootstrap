const base = (import.meta as any).env.VITE_API_URL ?? 'http://localhost:8000';

export async function api<T>(path: string, init: RequestInit = {}): Promise<T> {
  const res = await fetch(`${base}${path}`, init);
  const contentType = res.headers.get('content-type') || '';

  if (!res.ok) {
    // Normalize to { status, detail } without reading body twice
    if (contentType.includes('application/json')) {
      let data: any = null;
      try {
        data = await res.json();
      } catch {
        // fall back to text below
      }
      if (data !== null) {
        const detail = typeof data?.detail === 'string'
          ? data.detail
          : Array.isArray(data?.detail)
            ? data.detail.map((d: any) => d?.msg || d).join('; ')
            : JSON.stringify(data);
        throw { status: res.status, detail };
      }
    }
    const text = await res.text().catch(() => '');
    throw { status: res.status, detail: text || res.statusText };
  }

  if (contentType.includes('application/json')) {
    return res.json() as Promise<T>;
  }
  // Non-JSON response: return undefined as T
  return undefined as unknown as T;
}


