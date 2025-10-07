============================================================
DECISION TREE CONSTRUCTION DEMO
============================================================
Total samples: 958
Training samples: 766
Testing samples: 192

Constructing decision tree using training data...

🌳 Decision tree construction completed using PYTORCH!

🌲 DECISION TREE STRUCTURE
============================================================
Root [middle-middle-square] (gain: 0.0834)
├── = 0:
│   ├── [bottom-left-square] (gain: 0.1056)
│   ├── = 0:
│   │   ├── [top-right-square] (gain: 0.9024)
│   │   ├── = 1:
│   │   │   ├── Class 0
│   │   └── = 2:
│   │       ├── Class 1
│   ├── = 1:
│   │   ├── [top-right-square] (gain: 0.2782)
│   │   ├── = 0:
│   │   │   ├── Class 0
│   │   ├── = 1:
│   │   │   ├── Class 0
│   │   └── = 2:
│   │       ├── [top-left-square] (gain: 0.1767)
│   │       ├── = 0:
│   │       │   ├── [bottom-right-square] (gain: 0.9183)
│   │       │   ├── = 1:
│   │       │   │   ├── Class 0
│   │       │   └── = 2:
│   │       │       ├── Class 1
│   │       ├── = 1:
│   │       │   ├── [top-middle-square] (gain: 0.6058)
│   │       │   ├── = 0:
│   │       │   │   ├── [middle-left-square] (gain: 0.9183)
│   │       │   │   ├── = 1:
│   │       │   │   │   ├── Class 0
│   │       │   │   └── = 2:
│   │       │   │       ├── Class 1
│   │       │   ├── = 1:
│   │       │   │   ├── Class 1
│   │       │   └── = 2:
│   │       │       ├── Class 0
│   │       └── = 2:
│   │           ├── [top-middle-square] (gain: 0.3392)
│   │           ├── = 0:
│   │           │   ├── [middle-left-square] (gain: 0.9183)
│   │           │   ├── = 0:
│   │           │   │   ├── Class 0
│   │           │   ├── = 1:
│   │           │   │   ├── Class 1
│   │           │   └── = 2:
│   │           │       ├── Class 0
│   │           ├── = 1:
│   │           │   ├── [middle-left-square] (gain: 0.9183)
│   │           │   ├── = 0:
│   │           │   │   ├── Class 1
│   │           │   ├── = 1:
│   │           │   │   ├── Class 1
│   │           │   └── = 2:
│   │           │       ├── Class 0
│   │           └── = 2:
│   │               ├── Class 1
│   └── = 2:
│       ├── [top-right-square] (gain: 0.1225)
│       ├── = 0:
│       │   ├── Class 1
│       ├── = 1:
│       │   ├── [middle-right-square] (gain: 0.1682)
│       │   ├── = 0:
│       │   │   ├── Class 1
│       │   ├── = 1:
│       │   │   ├── [bottom-right-square] (gain: 0.9403)
│       │   │   ├── = 0:
│       │   │   │   ├── Class 1
│       │   │   ├── = 1:
│       │   │   │   ├── Class 0
│       │   │   └── = 2:
│       │   │       ├── Class 1
│       │   └── = 2:
│       │       ├── [top-left-square] (gain: 0.9183)
│       │       ├── = 0:
│       │       │   ├── Class 1
│       │       ├── = 1:
│       │       │   ├── Class 0
│       │       └── = 2:
│       │           ├── Class 1
│       └── = 2:
│           ├── Class 1
├── = 1:
│   ├── [top-right-square] (gain: 0.0223)
│   ├── = 0:
│   │   ├── [bottom-left-square] (gain: 0.2247)
│   │   ├── = 0:
│   │   │   ├── Class 0
│   │   ├── = 1:
│   │   │   ├── Class 0
│   │   └── = 2:
│   │       ├── [middle-right-square] (gain: 0.1159)
│   │       ├── = 0:
│   │       │   ├── [top-middle-square] (gain: 0.1772)
│   │       │   ├── = 0:
│   │       │   │   ├── Class 1
│   │       │   ├── = 1:
│   │       │   │   ├── [bottom-middle-square] (gain: 0.7219)
│   │       │   │   ├── = 1:
│   │       │   │   │   ├── Class 0
│   │       │   │   └── = 2:
│   │       │   │       ├── Class 1
│   │       │   └── = 2:
│   │       │       ├── [middle-left-square] (gain: 0.5000)
│   │       │       ├── = 0:
│   │       │       │   ├── Class 0
│   │       │       ├── = 1:
│   │       │       │   ├── Class 1
│   │       │       └── = 2:
│   │       │           ├── [top-left-square] (gain: 1.0000)
│   │       │           ├── = 1:
│   │       │           │   ├── Class 0
│   │       │           └── = 2:
│   │       │               ├── Class 1
│   │       ├── = 1:
│   │       │   ├── [middle-left-square] (gain: 0.9887)
│   │       │   ├── = 0:
│   │       │   │   ├── Class 1
│   │       │   ├── = 1:
│   │       │   │   ├── Class 0
│   │       │   └── = 2:
│   │       │       ├── Class 1
│   │       └── = 2:
│   │           ├── [bottom-middle-square] (gain: 0.2400)
│   │           ├── = 0:
│   │           │   ├── [top-left-square] (gain: 1.0000)
│   │           │   ├── = 1:
│   │           │   │   ├── Class 0
│   │           │   └── = 2:
│   │           │       ├── Class 1
│   │           ├── = 1:
│   │           │   ├── Class 0
│   │           └── = 2:
│   │               ├── [bottom-right-square] (gain: 0.9710)
│   │               ├── = 1:
│   │               │   ├── Class 0
│   │               └── = 2:
│   │                   ├── Class 1
│   ├── = 1:
│   │   ├── [bottom-left-square] (gain: 0.4759)
│   │   ├── = 0:
│   │   │   ├── Class 0
│   │   ├── = 1:
│   │   │   ├── Class 0
│   │   └── = 2:
│   │       ├── [top-middle-square] (gain: 0.1974)
│   │       ├── = 0:
│   │       │   ├── Class 1
│   │       ├── = 1:
│   │       │   ├── [top-left-square] (gain: 0.3436)
│   │       │   ├── = 0:
│   │       │   │   ├── [bottom-middle-square] (gain: 0.9183)
│   │       │   │   ├── = 1:
│   │       │   │   │   ├── Class 0
│   │       │   │   └── = 2:
│   │       │   │       ├── Class 1
│   │       │   ├── = 1:
│   │       │   │   ├── Class 0
│   │       │   └── = 2:
│   │       │       ├── [bottom-middle-square] (gain: 0.5917)
│   │       │       ├── = 0:
│   │       │       │   ├── Class 1
│   │       │       ├── = 1:
│   │       │       │   ├── Class 0
│   │       │       └── = 2:
│   │       │           ├── Class 1
│   │       └── = 2:
│   │           ├── [bottom-right-square] (gain: 0.1245)
│   │           ├── = 0:
│   │           │   ├── [middle-left-square] (gain: 0.9183)
│   │           │   ├── = 1:
│   │           │   │   ├── Class 0
│   │           │   └── = 2:
│   │           │       ├── Class 1
│   │           ├── = 1:
│   │           │   ├── [bottom-middle-square] (gain: 0.5613)
│   │           │   ├── = 0:
│   │           │   │   ├── [top-left-square] (gain: 1.0000)
│   │           │   │   ├── = 1:
│   │           │   │   │   ├── Class 0
│   │           │   │   └── = 2:
│   │           │   │       ├── Class 1
│   │           │   ├── = 1:
│   │           │   │   ├── Class 1
│   │           │   └── = 2:
│   │           │       ├── Class 0
│   │           └── = 2:
│   │               ├── [bottom-middle-square] (gain: 0.6122)
│   │               ├── = 0:
│   │               │   ├── Class 0
│   │               ├── = 1:
│   │               │   ├── [middle-right-square] (gain: 0.9183)
│   │               │   ├── = 1:
│   │               │   │   ├── Class 1
│   │               │   └── = 2:
│   │               │       ├── Class 0
│   │               └── = 2:
│   │                   ├── Class 1
│   └── = 2:
│       ├── [bottom-right-square] (gain: 0.0776)
│       ├── = 0:
│       │   ├── [top-left-square] (gain: 0.3462)
│       │   ├── = 0:
│       │   │   ├── Class 0
│       │   ├── = 1:
│       │   │   ├── Class 0
│       │   └── = 2:
│       │       ├── [top-middle-square] (gain: 0.7008)
│       │       ├── = 0:
│       │       │   ├── Class 0
│       │       ├── = 1:
│       │       │   ├── [middle-right-square] (gain: 0.7219)
│       │       │   ├── = 0:
│       │       │   │   ├── Class 0
│       │       │   ├── = 1:
│       │       │   │   ├── Class 1
│       │       │   └── = 2:
│       │       │       ├── Class 0
│       │       └── = 2:
│       │           ├── Class 1
│       ├── = 1:
│       │   ├── [top-left-square] (gain: 0.5439)
│       │   ├── = 0:
│       │   │   ├── Class 0
│       │   ├── = 1:
│       │   │   ├── Class 0
│       │   └── = 2:
│       │       ├── [top-middle-square] (gain: 0.4688)
│       │       ├── = 0:
│       │       │   ├── [bottom-middle-square] (gain: 0.9183)
│       │       │   ├── = 0:
│       │       │   │   ├── Class 1
│       │       │   ├── = 1:
│       │       │   │   ├── Class 0
│       │       │   └── = 2:
│       │       │       ├── Class 0
│       │       ├── = 1:
│       │       │   ├── [middle-right-square] (gain: 0.9183)
│       │       │   ├── = 0:
│       │       │   │   ├── Class 1
│       │       │   ├── = 1:
│       │       │   │   ├── Class 1
│       │       │   └── = 2:
│       │       │       ├── Class 0
│       │       └── = 2:
│       │           ├── Class 1
│       └── = 2:
│           ├── [middle-right-square] (gain: 0.4731)
│           ├── = 0:
│           │   ├── [top-middle-square] (gain: 0.6465)
│           │   ├── = 0:
│           │   │   ├── Class 1
│           │   ├── = 1:
│           │   │   ├── Class 0
│           │   └── = 2:
│           │       ├── [top-left-square] (gain: 0.8113)
│           │       ├── = 1:
│           │       │   ├── Class 0
│           │       └── = 2:
│           │           ├── Class 1
│           ├── = 1:
│           │   ├── [middle-left-square] (gain: 0.3995)
│           │   ├── = 0:
│           │   │   ├── [bottom-middle-square] (gain: 0.8113)
│           │   │   ├── = 0:
│           │   │   │   ├── Class 1
│           │   │   ├── = 1:
│           │   │   │   ├── Class 0
│           │   │   └── = 2:
│           │   │       ├── Class 1
│           │   ├── = 1:
│           │   │   ├── Class 0
│           │   └── = 2:
│           │       ├── [top-middle-square] (gain: 0.8113)
│           │       ├── = 1:
│           │       │   ├── Class 0
│           │       └── = 2:
│           │           ├── Class 1
│           └── = 2:
│               ├── Class 1
├── = 2:
│   ├── [bottom-right-square] (gain: 0.0270)
│   ├── = 0:
│   │   ├── [top-left-square] (gain: 0.1239)
│   │   ├── = 0:
│   │   │   ├── Class 1
│   │   ├── = 1:
│   │   │   ├── [bottom-middle-square] (gain: 0.1032)
│   │   │   ├── = 0:
│   │   │   │   ├── [middle-left-square] (gain: 0.1605)
│   │   │   │   ├── = 0:
│   │   │   │   │   ├── Class 1
│   │   │   │   ├── = 1:
│   │   │   │   │   ├── [bottom-left-square] (gain: 1.0000)
│   │   │   │   │   ├── = 1:
│   │   │   │   │   │   ├── Class 0
│   │   │   │   │   └── = 2:
│   │   │   │   │       ├── Class 1
│   │   │   │   └── = 2:
│   │   │   │       ├── [middle-right-square] (gain: 0.5917)
│   │   │   │       ├── = 0:
│   │   │   │       │   ├── Class 0
│   │   │   │       ├── = 1:
│   │   │   │       │   ├── Class 1
│   │   │   │       └── = 2:
│   │   │   │           ├── Class 1
│   │   │   ├── = 1:
│   │   │   │   ├── Class 1
│   │   │   └── = 2:
│   │   │       ├── [top-middle-square] (gain: 0.4591)
│   │   │       ├── = 0:
│   │   │       │   ├── [middle-right-square] (gain: 0.9183)
│   │   │       │   ├── = 0:
│   │   │       │   │   ├── Class 0
│   │   │       │   ├── = 1:
│   │   │       │   │   ├── Class 1
│   │   │       │   └── = 2:
│   │   │       │       ├── Class 0
│   │   │       ├── = 1:
│   │   │       │   ├── [top-right-square] (gain: 0.6122)
│   │   │       │   ├── = 0:
│   │   │       │   │   ├── Class 1
│   │   │       │   ├── = 1:
│   │   │       │   │   ├── Class 0
│   │   │       │   └── = 2:
│   │   │       │       ├── [middle-right-square] (gain: 0.9183)
│   │   │       │       ├── = 0:
│   │   │       │       │   ├── Class 1
│   │   │       │       ├── = 1:
│   │   │       │       │   ├── Class 1
│   │   │       │       └── = 2:
│   │   │       │           ├── Class 0
│   │   │       └── = 2:
│   │   │           ├── Class 1
│   │   └── = 2:
│   │       ├── Class 1
│   ├── = 1:
│   │   ├── [top-left-square] (gain: 0.0713)
│   │   ├── = 0:
│   │   │   ├── [middle-right-square] (gain: 0.0760)
│   │   │   ├── = 0:
│   │   │   │   ├── [bottom-left-square] (gain: 0.2454)
│   │   │   │   ├── = 0:
│   │   │   │   │   ├── Class 1
│   │   │   │   ├── = 1:
│   │   │   │   │   ├── [bottom-middle-square] (gain: 0.9710)
│   │   │   │   │   ├── = 1:
│   │   │   │   │   │   ├── Class 0
│   │   │   │   │   └── = 2:
│   │   │   │   │       ├── Class 1
│   │   │   │   └── = 2:
│   │   │   │       ├── Class 1
│   │   │   ├── = 1:
│   │   │   │   ├── [top-right-square] (gain: 0.7207)
│   │   │   │   ├── = 0:
│   │   │   │   │   ├── Class 1
│   │   │   │   ├── = 1:
│   │   │   │   │   ├── Class 0
│   │   │   │   └── = 2:
│   │   │   │       ├── [middle-left-square] (gain: 0.3060)
│   │   │   │       ├── = 0:
│   │   │   │       │   ├── Class 1
│   │   │   │       ├── = 1:
│   │   │   │       │   ├── Class 1
│   │   │   │       └── = 2:
│   │   │   │           ├── [top-middle-square] (gain: 1.0000)
│   │   │   │           ├── = 0:
│   │   │   │           │   ├── Class 1
│   │   │   │           └── = 2:
│   │   │   │               ├── Class 0
│   │   │   └── = 2:
│   │   │       ├── [middle-left-square] (gain: 0.2293)
│   │   │       ├── = 0:
│   │   │       │   ├── [top-middle-square] (gain: 0.5000)
│   │   │       │   ├── = 0:
│   │   │       │   │   ├── Class 0
│   │   │       │   ├── = 1:
│   │   │       │   │   ├── Class 1
│   │   │       │   └── = 2:
│   │   │       │       ├── [top-right-square] (gain: 1.0000)
│   │   │       │       ├── = 0:
│   │   │       │       │   ├── Class 0
│   │   │       │       └── = 1:
│   │   │       │           ├── Class 1
│   │   │       ├── = 1:
│   │   │       │   ├── [bottom-left-square] (gain: 0.3219)
│   │   │       │   ├── = 0:
│   │   │       │   │   ├── Class 1
│   │   │       │   ├── = 1:
│   │   │       │   │   ├── [top-right-square] (gain: 1.0000)
│   │   │       │   │   ├── = 0:
│   │   │       │   │   │   ├── Class 1
│   │   │       │   │   └── = 2:
│   │   │       │   │       ├── Class 0
│   │   │       │   └── = 2:
│   │   │       │       ├── Class 1
│   │   │       └── = 2:
│   │   │           ├── Class 1
│   │   ├── = 1:
│   │   │   ├── [bottom-left-square] (gain: 0.1145)
│   │   │   ├── = 0:
│   │   │   │   ├── Class 1
│   │   │   ├── = 1:
│   │   │   │   ├── [middle-left-square] (gain: 0.3407)
│   │   │   │   ├── = 0:
│   │   │   │   │   ├── [bottom-middle-square] (gain: 0.9183)
│   │   │   │   │   ├── = 1:
│   │   │   │   │   │   ├── Class 0
│   │   │   │   │   └── = 2:
│   │   │   │   │       ├── Class 1
│   │   │   │   ├── = 1:
│   │   │   │   │   ├── Class 0
│   │   │   │   └── = 2:
│   │   │   │       ├── [bottom-middle-square] (gain: 0.6500)
│   │   │   │       ├── = 0:
│   │   │   │       │   ├── Class 1
│   │   │   │       ├── = 1:
│   │   │   │       │   ├── Class 0
│   │   │   │       └── = 2:
│   │   │   │           ├── Class 1
│   │   │   └── = 2:
│   │   │       ├── [top-right-square] (gain: 0.1913)
│   │   │       ├── = 0:
│   │   │       │   ├── Class 1
│   │   │       ├── = 1:
│   │   │       │   ├── [top-middle-square] (gain: 0.3774)
│   │   │       │   ├── = 0:
│   │   │       │   │   ├── Class 1
│   │   │       │   ├── = 1:
│   │   │       │   │   ├── Class 0
│   │   │       │   └── = 2:
│   │   │       │       ├── [middle-right-square] (gain: 0.8113)
│   │   │       │       ├── = 0:
│   │   │       │       │   ├── Class 1
│   │   │       │       ├── = 1:
│   │   │       │       │   ├── Class 0
│   │   │       │       └── = 2:
│   │   │       │           ├── Class 1
│   │   │       └── = 2:
│   │   │           ├── Class 1
│   │   └── = 2:
│   │       ├── [top-right-square] (gain: 0.0821)
│   │       ├── = 0:
│   │       │   ├── [bottom-left-square] (gain: 0.3436)
│   │       │   ├── = 0:
│   │       │   │   ├── Class 1
│   │       │   ├── = 1:
│   │       │   │   ├── [bottom-middle-square] (gain: 0.9852)
│   │       │   │   ├── = 0:
│   │       │   │   │   ├── Class 1
│   │       │   │   ├── = 1:
│   │       │   │   │   ├── Class 0
│   │       │   │   └── = 2:
│   │       │   │       ├── Class 1
│   │       │   └── = 2:
│   │       │       ├── Class 1
│   │       ├── = 1:
│   │       │   ├── [middle-right-square] (gain: 0.4301)
│   │       │   ├── = 0:
│   │       │   │   ├── [bottom-middle-square] (gain: 0.9183)
│   │       │   │   ├── = 0:
│   │       │   │   │   ├── Class 1
│   │       │   │   ├── = 1:
│   │       │   │   │   ├── Class 0
│   │       │   │   └── = 2:
│   │       │   │       ├── Class 1
│   │       │   ├── = 1:
│   │       │   │   ├── Class 0
│   │       │   └── = 2:
│   │       │       ├── [middle-left-square] (gain: 0.6100)
│   │       │       ├── = 0:
│   │       │       │   ├── Class 0
│   │       │       ├── = 1:
│   │       │       │   ├── [bottom-left-square] (gain: 0.9183)
│   │       │       │   ├── = 1:
│   │       │       │   │   ├── Class 1
│   │       │       │   └── = 2:
│   │       │       │       ├── Class 0
│   │       │       └── = 2:
│   │       │           ├── Class 1
│   │       └── = 2:
│   │           ├── [bottom-left-square] (gain: 0.5549)
│   │           ├── = 0:
│   │           │   ├── Class 1
│   │           ├── = 1:
│   │           │   ├── [top-middle-square] (gain: 0.8113)
│   │           │   ├── = 0:
│   │           │   │   ├── Class 0
│   │           │   ├── = 1:
│   │           │   │   ├── Class 0
│   │           │   └── = 2:
│   │           │       ├── Class 1
│   │           └── = 2:
│   │               ├── Class 1
│   └── = 2:
│       ├── [top-left-square] (gain: 0.2780)
│       ├── = 0:
│       │   ├── Class 1
│       ├── = 1:
│       │   ├── [middle-right-square] (gain: 0.0689)
│       │   ├── = 0:
│       │   │   ├── [bottom-left-square] (gain: 0.1984)
│       │   │   ├── = 0:
│       │   │   │   ├── Class 0
│       │   │   ├── = 1:
│       │   │   │   ├── [middle-left-square] (gain: 0.5917)
│       │   │   │   ├── = 0:
│       │   │   │   │   ├── Class 1
│       │   │   │   ├── = 1:
│       │   │   │   │   ├── Class 0
│       │   │   │   └── = 2:
│       │   │   │       ├── Class 0
│       │   │   └── = 2:
│       │   │       ├── [middle-left-square] (gain: 0.9710)
│       │   │       ├── = 0:
│       │   │       │   ├── Class 0
│       │   │       ├── = 1:
│       │   │       │   ├── Class 1
│       │   │       └── = 2:
│       │   │           ├── Class 0
│       │   ├── = 1:
│       │   │   ├── [middle-left-square] (gain: 0.4046)
│       │   │   ├── = 0:
│       │   │   │   ├── Class 1
│       │   │   ├── = 1:
│       │   │   │   ├── [bottom-left-square] (gain: 0.9183)
│       │   │   │   ├── = 1:
│       │   │   │   │   ├── Class 0
│       │   │   │   └── = 2:
│       │   │   │       ├── Class 1
│       │   │   └── = 2:
│       │   │       ├── [bottom-left-square] (gain: 0.0760)
│       │   │       ├── = 0:
│       │   │       │   ├── Class 0
│       │   │       ├── = 1:
│       │   │       │   ├── [top-right-square] (gain: 0.9183)
│       │   │       │   ├── = 1:
│       │   │       │   │   ├── Class 1
│       │   │       │   └── = 2:
│       │   │       │       ├── Class 0
│       │   │       └── = 2:
│       │   │           ├── [top-right-square] (gain: 0.9183)
│       │   │           ├── = 1:
│       │   │           │   ├── Class 0
│       │   │           └── = 2:
│       │   │               ├── Class 1
│       │   └── = 2:
│       │       ├── [middle-left-square] (gain: 0.3425)
│       │       ├── = 0:
│       │       │   ├── [top-right-square] (gain: 0.9710)
│       │       │   ├── = 1:
│       │       │   │   ├── Class 0
│       │       │   └── = 2:
│       │       │       ├── Class 1
│       │       ├── = 1:
│       │       │   ├── [top-right-square] (gain: 0.9183)
│       │       │   ├── = 0:
│       │       │   │   ├── Class 0
│       │       │   ├── = 1:
│       │       │   │   ├── Class 0
│       │       │   └── = 2:
│       │       │       ├── Class 1
│       │       └── = 2:
│       │           ├── Class 1
│       └── = 2:
│           ├── Class 1


📊 OVERALL PERFORMANCE METRICS
========================================
Accuracy:             0.8723 (87.23%)
Precision (weighted): 0.8734
Recall (weighted):    0.8723
F1-Score (weighted):  0.8728
Precision (macro):    0.8586
Recall (macro):       0.8634
F1-Score (macro):     0.8609

🌳 TREE COMPLEXITY METRICS
========================================
Maximum Depth:        7
Total Nodes:          283
Leaf Nodes:           181
Internal Nodes:       102