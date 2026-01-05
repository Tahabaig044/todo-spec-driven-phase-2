'use client';

import { useState, useEffect } from 'react';
import TaskList from '../components/TaskList';
// import TaskForm from '@/components/TaskForm';
import { Task } from '../types/task';
import { getTasks, createTask, updateTask, deleteTask, toggleTaskCompletion } from '../services/api';
// import { TaskContextProvider, useTaskContext } from '@/context/TaskContext';
import TaskForm from '../components/TaskForm';
import { TaskContextProvider } from '../context/TaskContext';

export default function Home() {
  return (
    <TaskContextProvider>
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-4xl mx-auto px-4">
          <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">Todo Application</h1>
          <TaskForm />
          <TaskList />
        </div>
      </div>
    </TaskContextProvider>
  );
}