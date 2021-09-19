export interface Event {
  id: string
  name: string
  location: string
  reward: number
  start_at: Date
  end_at: Date
  description: string
  is_valid: boolean
  event_picture: string
}
