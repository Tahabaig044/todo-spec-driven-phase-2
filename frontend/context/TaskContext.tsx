'use client';

import { createContext, useContext, useReducer, ReactNode, useEffect } from 'react';
import { Task, TaskInput } from '../types/task';
import { getTasks, createTask, updateTask, deleteTask, toggleTaskCompletion as toggleTaskCompletionApi } from '../services/api';

type TaskState = {
  tasks: Task[];
  loading: boolean;
  error: string | null;
};

type TaskAction =
  | { type: 'FETCH_TASKS_START' }
  | { type: 'FETCH_TASKS_SUCCESS'; payload: Task[] }
  | { type: 'FETCH_TASKS_ERROR'; payload: string }
  | { type: 'ADD_TASK_SUCCESS'; payload: Task }
  | { type: 'UPDATE_TASK_SUCCESS'; payload: Task }
  | { type: 'DELETE_TASK_SUCCESS'; payload: number }
  | { type: 'TOGGLE_TASK_COMPLETION_SUCCESS'; payload: Task };

const initialState: TaskState = {
  tasks: [],
  loading: false,
  error: null,
};

const taskReducer = (state: TaskState, action: TaskAction): TaskState => {
  switch (action.type) {
    case 'FETCH_TASKS_START':
      return { ...state, loading: true, error: null };
    case 'FETCH_TASKS_SUCCESS':
      return { ...state, loading: false, tasks: action.payload };
    case 'FETCH_TASKS_ERROR':
      return { ...state, loading: false, error: action.payload };
    case 'ADD_TASK_SUCCESS':
      return { ...state, tasks: [...state.tasks, action.payload] };
    case 'UPDATE_TASK_SUCCESS':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.id ? action.payload : task
        ),
      };
    case 'DELETE_TASK_SUCCESS':
      return {
        ...state,
        tasks: state.tasks.filter(task => task.id !== action.payload),
      };
    case 'TOGGLE_TASK_COMPLETION_SUCCESS':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.id ? action.payload : task
        ),
      };
    default:
      return state;
  }
};

type TaskContextType = {
  tasks: Task[];
  loading: boolean;
  error: string | null;
  addTask: (taskData: TaskInput) => Promise<void>;
  updateTask: (id: number, taskData: Partial<TaskInput>) => Promise<void>;
  deleteTask: (id: number) => Promise<void>;
  toggleTaskCompletion: (id: number) => Promise<void>;
};

const TaskContext = createContext<TaskContextType | undefined>(undefined);

export const TaskContextProvider = ({ children }: { children: ReactNode }) => {
  const [state, dispatch] = useReducer(taskReducer, initialState);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      dispatch({ type: 'FETCH_TASKS_START' });
      const tasks = await getTasks();
      dispatch({ type: 'FETCH_TASKS_SUCCESS', payload: tasks });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Failed to fetch tasks';
      dispatch({ type: 'FETCH_TASKS_ERROR', payload: errorMessage });
    }
  };

  const addTask = async (taskData: TaskInput) => {
    try {
      const newTask = await createTask(taskData);
      dispatch({ type: 'ADD_TASK_SUCCESS', payload: newTask });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Failed to add task';
      dispatch({ type: 'FETCH_TASKS_ERROR', payload: errorMessage });
      throw error;
    }
  };

  const updateTask = async (id: number, taskData: Partial<TaskInput>) => {
    try {
      const updatedTask = await updateTask(id, taskData);
      dispatch({ type: 'UPDATE_TASK_SUCCESS', payload: updatedTask });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Failed to update task';
      dispatch({ type: 'FETCH_TASKS_ERROR', payload: errorMessage });
      throw error;
    }
  };

  const deleteTask = async (id: number) => {
    try {
      await deleteTask(id);
      dispatch({ type: 'DELETE_TASK_SUCCESS', payload: id });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Failed to delete task';
      dispatch({ type: 'FETCH_TASKS_ERROR', payload: errorMessage });
      throw error;
    }
  };

  const toggleTaskCompletion = async (id: number) => {
    try {
      const updatedTask = await toggleTaskCompletionApi(id);
      dispatch({ type: 'TOGGLE_TASK_COMPLETION_SUCCESS', payload: updatedTask });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Failed to toggle task completion';
      dispatch({ type: 'FETCH_TASKS_ERROR', payload: errorMessage });
      throw error;
    }
  };

  return (
    <TaskContext.Provider
      value={{
        tasks: state.tasks,
        loading: state.loading,
        error: state.error,
        addTask,
        updateTask,
        deleteTask,
        toggleTaskCompletion,
      }}
    >
      {children}
    </TaskContext.Provider>
  );
};

export const useTaskContext = () => {
  const context = useContext(TaskContext);
  if (context === undefined) {
    throw new Error('useTaskContext must be used within a TaskContextProvider');
  }
  return context;
};