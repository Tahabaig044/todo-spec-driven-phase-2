import { Task, TaskInput } from '../types/task';

// API base URL - can be configured via environment variables
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

// Helper function to handle API responses
const handleResponse = async (response: Response) => {
  // Read as text first to safely handle empty bodies (e.g. 204 No Content)
  const text = await response.text();

  if (!response.ok) {
    let errorData: any = {};
    if (text) {
      try {
        errorData = JSON.parse(text);
      } catch (e) {
        // ignore parse errors and fall back to generic error
      }
    }
    throw new Error(errorData?.detail || `HTTP error! status: ${response.status}`);
  }

  if (!text) return null;

  try {
    return JSON.parse(text);
  } catch (e) {
    // If response isn't valid JSON, return null rather than throwing JSON parse error
    return null;
  }
};

export const getTasks = async (): Promise<Task[]> => {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  return handleResponse(response);
};

export const getTaskById = async (id: number): Promise<Task> => {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`);
  return handleResponse(response);
};

export const createTask = async (taskData: TaskInput): Promise<Task> => {
  const response = await fetch(`${API_BASE_URL}/tasks`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(taskData),
  });
  return handleResponse(response);
};

export const updateTask = async (id: number, taskData: Partial<TaskInput>): Promise<Task> => {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(taskData),
  });
  return handleResponse(response);
};

export const deleteTask = async (id: number): Promise<void> => {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: 'DELETE',
  });
  await handleResponse(response);
};

export const toggleTaskCompletion = async (id: number): Promise<Task> => {
  // First get the current task to get its current completion status
  const currentTask = await getTaskById(id);

  // Then update the completion status
  return updateTask(id, { completed: !currentTask.completed });
};