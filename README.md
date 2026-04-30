<div align="center">
  
  # LeetCode Journey
  
  *A curated collection of algorithmic solutions, data structures, and problem-solving patterns.*

  [![LeetCode Stats](https://img.shields.io/badge/LeetCode-5VPjMsfuqV-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/5VPjMsfuqV/)
  [![Sync Submissions](https://img.shields.io/github/actions/workflow/status/AyushSingh360/Leetcode/leetcode-sync.yml?label=Sync%20Status&style=for-the-badge&color=2ea44f)](https://github.com/AyushSingh360/Leetcode/actions)

  <br />
  <br />

  <a href="https://leetcode.com/u/5VPjMsfuqV/">
    <img src="https://leetcard.jacoblin.cool/5VPjMsfuqV?theme=dark&font=Inter" alt="LeetCode Stats Chart" />
  </a>

</div>

<br />

## Overview

This workspace serves as a personal archive for competitive programming and interview preparation. All accepted submissions are automatically synced from the LeetCode profile to this repository via GitHub Actions, ensuring that progress is continuously documented and version-controlled.

<br />

## Automation Architecture

The synchronization process is fully automated. Below is the architectural flow of how solutions are captured and stored in the repository.

```mermaid
flowchart LR
    subgraph Platform
        LC((LeetCode))
    end

    subgraph Pipeline
        Trigger([Cron Schedule]) --> Action[GitHub Action]
        Dispatch([Manual Trigger]) --> Action
        Action --> |Authenticates| Fetch[Fetch API]
        Fetch --> |Retrieves| Data{Accepted Code}
    end

    subgraph Version Control
        Data --> Commit[Git Commit]
        Commit --> Repo[(Repository)]
    end

    LC -.->|Provides Data| Fetch
```

<br />

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── leetcode-sync.yml    # Synchronization automation pipeline
├── leetcode/                    # Auto-populated directory of solutions
└── README.md                    # Project documentation
```

<br />

## Connect

- **LeetCode Profile:** [leetcode.com/u/5VPjMsfuqV](https://leetcode.com/u/5VPjMsfuqV/)
- **GitHub Profile:** [@AyushSingh360](https://github.com/AyushSingh360)

---
<div align="center">
  <p><i>Keep Coding. Keep Improving.</i></p>
</div>
