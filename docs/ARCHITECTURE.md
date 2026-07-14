# TinyVerse Kids Studio Architecture

## Overview

TinyVerse Kids Studio is an AI-powered platform that automatically creates educational YouTube videos for children.

The platform follows a modular architecture where every component has a single responsibility.

---

## High-Level Architecture

```
User
   │
   ▼
FastAPI API
   │
   ▼
Episode Orchestrator
   │
   ├──────────────┬───────────────┬───────────────┐
   ▼              ▼               ▼               ▼
LessonAgent   StoryAgent     QuizAgent      SongAgent
   │
   ▼
AI Provider
   │
   ├──────────────┬───────────────┬───────────────┐
   ▼              ▼               ▼               ▼
Mock         Gemini         Claude         OpenAI
```

---

## Responsibilities

### API

Receives requests from clients.

### Episode Orchestrator

Coordinates the complete episode generation process.

### Agents

Each agent performs one task only.

- Lesson Agent
- Story Agent
- Scene Agent
- Image Agent
- Quiz Agent
- Song Agent

### Providers

Responsible for communicating with external AI models.

### Services

Reusable helper logic such as:

- Prompt loading
- Video rendering
- Storage
- Logging

### Schemas

Define request and response models.

---

## Future Pipeline

```
Topic

↓

Lesson Plan

↓

Story

↓

Scenes

↓

Image Prompts

↓

Voice

↓

Music

↓

Subtitles

↓

Video Rendering

↓

Thumbnail

↓

YouTube Upload
```
