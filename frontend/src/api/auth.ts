import { api } from './client'

export type TokenResponse = { access_token: string; token_type: string }

export async function createUser(body: {username: string; email: string; password: string; role?: string}) {
  return api('/users/', { method: 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(body) });
}

export async function login(username: string, password: string): Promise<TokenResponse> {
  const form = new URLSearchParams({ username, password });
  return api('/auth/token', { method: 'POST', headers: {'Content-Type':'application/x-www-form-urlencoded'}, body: form.toString() });
}

export async function getMe(token: string) {
  return api('/auth/users/me', { headers: { Authorization: `Bearer ${token}` }});
}


