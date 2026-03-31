import streamlit as st

st.set_page_config(
    page_title="Vilaj De Dye – Escape the Crossfire",
    page_icon="🏃‍♂️",
    layout="wide"
)

hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { margin-top: -50px; }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

GAME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>Vilaj De Dye - Escape the Crossfire</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background: linear-gradient(145deg, #0a0f1e 0%, #03060c 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            font-family: 'Courier New', 'Poppins', monospace;
            padding: 12px;
        }

        .game-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 12px;
            width: 100%;
            max-width: 1000px;
            margin: auto;
        }

        canvas {
            display: block;
            margin: 0 auto;
            border-radius: 28px;
            box-shadow: 0 20px 35px rgba(0, 0, 0, 0.6), inset 0 0 4px rgba(255, 255, 255, 0.1);
            cursor: none;
            width: 100%;
            height: auto;
            background: #1f2a2e;
        }

        .start-screen {
            position: relative;
            width: 100%;
            max-width: 1000px;
            max-height: 90vh;
            overflow-y: auto;
            background: radial-gradient(circle at 30% 20%, #0b2b3b, #01050e);
            border-radius: 28px;
            box-shadow: 0 20px 35px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            backdrop-filter: blur(1px);
            padding: 20px 20px 40px 20px;
            margin: 0 auto;
        }

        .flag-container {
            position: relative;
            width: 80%;
            max-width: 360px;
            height: auto;
            aspect-ratio: 360 / 200;
            margin-bottom: 20px;
            animation: floatFlag 2.8s infinite ease-in-out;
            filter: drop-shadow(0 10px 12px rgba(0,0,0,0.5));
        }

        .haitian-flag {
            width: 100%;
            height: 100%;
            background: linear-gradient(to bottom, #00209f 0%, #00209f 50%, #d21034 50%, #d21034 100%);
            border-radius: 12px;
            border: 3px solid gold;
            box-shadow: 0 0 18px rgba(255,215,0,0.6);
            position: relative;
        }

        .stars-field {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .star {
            position: absolute;
            background: radial-gradient(circle, #fff9c4, #ffec80);
            border-radius: 50%;
            opacity: 0.9;
            animation: twinkle 1.8s infinite alternate;
            box-shadow: 0 0 6px gold;
        }

        @keyframes floatFlag {
            0% { transform: translateY(0px) rotate(0deg);}
            50% { transform: translateY(-10px) rotate(0.6deg);}
            100% { transform: translateY(0px) rotate(0deg);}
        }

        @keyframes twinkle {
            0% { opacity: 0.3; transform: scale(0.8);}
            100% { opacity: 1; transform: scale(1.2);}
        }

        .info-panel-start {
            background: rgba(0,0,0,0.75);
            backdrop-filter: blur(4px);
            border-radius: 24px;
            padding: 15px 20px;
            margin: 10px 0;
            width: 95%;
            max-width: 500px;
            text-align: center;
            color: #ffefb9;
            border: 1px solid gold;
        }

        .info-panel-start h2 {
            font-size: clamp(20px, 6vw, 28px);
            margin-bottom: 8px;
            color: #f5e56b;
        }

        .info-panel-start p {
            margin: 6px 0;
            font-size: clamp(11px, 3.5vw, 14px);
        }

        .price-tag {
            background: #d62c1e;
            display: inline-block;
            padding: 5px 15px;
            border-radius: 40px;
            font-weight: bold;
            margin-top: 8px;
        }

        .password-area {
            margin: 15px 0;
            width: 90%;
            max-width: 300px;
            text-align: center;
        }

        .password-area input {
            width: 100%;
            padding: 14px;
            font-size: 18px;
            border-radius: 40px;
            border: 2px solid gold;
            background: rgba(0,0,0,0.7);
            color: #ffefb9;
            text-align: center;
            font-family: monospace;
            letter-spacing: 2px;
        }

        .password-area input:focus {
            outline: none;
            border-color: #ffaa33;
        }

        .error-msg {
            color: #ff8888;
            font-size: 12px;
            margin-top: 5px;
            background: rgba(0,0,0,0.5);
            display: inline-block;
            padding: 2px 10px;
            border-radius: 20px;
        }

        .start-btn {
            margin-top: 20px;
            background: #d62c1e;
            border: none;
            font-size: clamp(20px, 6vw, 28px);
            font-weight: bold;
            padding: 14px 30px;
            border-radius: 60px;
            color: #ffefb9;
            font-family: monospace;
            cursor: pointer;
            box-shadow: 0 8px 0 #631007;
            transition: 0.07s linear;
            letter-spacing: 2px;
        }

        .start-btn:active {
            transform: translateY(4px);
            box-shadow: 0 4px 0 #631007;
        }

        .game-area {
            display: none;
            flex-direction: column;
            align-items: center;
            width: 100%;
            margin-bottom: 20px;
        }

        .info-panel {
            width: 100%;
            background: #0f0e17cc;
            backdrop-filter: blur(8px);
            border-radius: 40px;
            padding: 8px 16px;
            display: flex;
            justify-content: space-between;
            color: #f7d44a;
            font-weight: bold;
            font-size: clamp(12px, 4vw, 18px);
            margin-bottom: 12px;
            border: 1px solid #ffcd7e;
            flex-wrap: wrap;
            gap: 8px;
        }

        .info-panel button {
            background: #2c2e3a;
            border: none;
            color: white;
            padding: 6px 14px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: bold;
        }

        .info-panel button:hover {
            background: #ff7b2c;
        }

        .controls-hint {
            background: #00000099;
            padding: 6px 12px;
            border-radius: 28px;
            font-size: clamp(10px, 3vw, 14px);
            text-align: center;
            margin-bottom: 15px;
        }

        .touch-controls {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 15px;
            flex-wrap: wrap;
        }

        .touch-btn {
            background: rgba(0,0,0,0.7);
            border: 2px solid gold;
            color: gold;
            font-size: 28px;
            font-weight: bold;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            user-select: none;
            touch-action: manipulation;
            transition: 0.05s linear;
        }

        .touch-btn:active {
            transform: scale(0.92);
            background: rgba(255,215,0,0.3);
        }

        .run-btn {
            background: #d62c1e;
            border-color: #ffaa66;
            color: white;
            font-size: 18px;
            width: 80px;
            border-radius: 40px;
        }

        @media (max-width: 600px) {
            .touch-btn {
                width: 60px;
                height: 60px;
                font-size: 24px;
            }
            .run-btn {
                width: 70px;
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
<div class="game-wrapper">
    <!-- START SCREEN -->
    <div id="startScreen" class="start-screen">
        <div class="flag-container">
            <div class="haitian-flag"></div>
            <div class="stars-field" id="starsField"></div>
        </div>

        <div class="info-panel-start">
            <h2>🔥 VILAJ DE DYE 🔥</h2>
            <p><strong>"Papa ak Twa Pitit Gason" — Escape the nightmare</strong></p>
        </div>

        <div class="info-panel-start">
            <p>🎮 <strong>Python Code Builder:</strong> Gesner Deslandes</p>
            <p>🏢 <strong>Company:</strong> GlobalInternet.py</p>
            <p>👨‍💻 <strong>Owner & Developer:</strong> Gesner Deslandes</p>
            <p>🇭🇹 <strong>Made in Haiti</strong> 🇭🇹</p>
            <p>📧 <strong>Contact:</strong> deslndes78@gmail.com</p>
            <p>📱 <strong>Moncash Payment:</strong> (509) 4738-5663 via Prisme Transfer</p>
            <p class="price-tag">💰 Reasonable price for online game sale – Contact us! 💰</p>
            <p style="font-size:12px; margin-top:10px;">© 2026 GlobalInternet.py – All rights reserved</p>
        </div>

        <div class="password-area">
            <input type="password" id="unlockPassword" placeholder="Enter password to unlock" autocomplete="off">
            <div id="passwordError" class="error-msg" style="display: none;">Wrong password. Try again.</div>
        </div>

        <button class="start-btn" id="startGameBtn">🔓 JWE (PLAY) 🔓</button>
        <div class="sub" style="font-size:12px; margin-top:12px;">⚡ Arrow keys / Touch buttons • Hold SHIFT/RUN to sprint ⚡</div>
    </div>

    <!-- GAME INTERFACE -->
    <div id="gameContainer" class="game-area">
        <div class="info-panel">
            <span>🔥 VILAJ DE DYE 🔥</span>
            <span>🏠 SAFE REFUGE → right side</span>
            <span id="gameStatusMsg">⚔️ ESCAPE ⚔️</span>
            <div style="display: flex; gap: 8px;">
                <button id="fullscreenBtn">⛶ FULLSCREEN</button>
                <button id="resetGameBtn">RESTART</button>
                <button id="logoutBtn">LOGOUT</button>
            </div>
        </div>
        <canvas id="gameCanvas" width="1000" height="600"></canvas>
        <div class="touch-controls">
            <div class="touch-btn" data-key="ArrowUp">▲</div>
            <div class="touch-btn" data-key="ArrowLeft">◀</div>
            <div class="touch-btn" data-key="ArrowDown">▼</div>
            <div class="touch-btn" data-key="ArrowRight">▶</div>
            <div class="touch-btn run-btn" data-key="Shift">🏃 RUN</div>
        </div>
        <div class="controls-hint">🎮 ARROWS = move | SHIFT = RUN | Avoid BULLETS! 🎮</div>
    </div>
</div>

<script>
    (function(){
        // ---------- DOM elements ----------
        const startScreenDiv = document.getElementById('startScreen');
        const gameContainer = document.getElementById('gameContainer');
        const startBtn = document.getElementById('startGameBtn');
        const resetBtn = document.getElementById('resetGameBtn');
        const logoutBtn = document.getElementById('logoutBtn');
        const fullscreenBtn = document.getElementById('fullscreenBtn');
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        const statusSpan = document.getElementById('gameStatusMsg');
        const passwordInput = document.getElementById('unlockPassword');
        const passwordError = document.getElementById('passwordError');

        // ---------- Game constants ----------
        const W = 1000, H = 600;
        const SAFE_ZONE_X = 870;
        const SAFE_ZONE_Y_MIN = 180;
        const SAFE_ZONE_Y_MAX = 450;

        const FATHER_RADIUS = 18;
        const SON_RADIUS = 13;
        const BULLET_RADIUS = 6;

        const WALK_SPEED = 2.8;
        const RUN_SPEED = 5.9;

        // ---------- Global game state ----------
        let gameActive = true;
        let gameWin = false;
        let gameOverFlag = false;
        let animationId = null;
        let autoRestartTimeout = null;
        
        let father = { x: 90, y: H/2, radius: FATHER_RADIUS };
        let sons = [
            { x: 70, y: H/2 - 18, radius: SON_RADIUS, offsetX: -24, offsetY: -15 },
            { x: 75, y: H/2 + 20, radius: SON_RADIUS, offsetX: -20, offsetY: 18 },
            { x: 55, y: H/2 + 5, radius: SON_RADIUS, offsetX: -32, offsetY: 2 }
        ];
        
        let bullets = [];
        
        let enemies = [
            { x: 150, y: 110, type: "bandit", cooldown: 0, shootDelay: 70 },
            { x: 220, y: 500, type: "bandit", cooldown: 0, shootDelay: 75 },
            { x: 480, y: 80, type: "bandit", cooldown: 0, shootDelay: 65 },
            { x: 650, y: 540, type: "police", cooldown: 0, shootDelay: 60 },
            { x: 780, y: 180, type: "police", cooldown: 0, shootDelay: 68 },
            { x: 830, y: 470, type: "police", cooldown: 0, shootDelay: 72 },
            { x: 540, y: 380, type: "bandit", cooldown: 0, shootDelay: 70 },
            { x: 370, y: 520, type: "police", cooldown: 0, shootDelay: 66 }
        ];
        
        const keys = { ArrowUp: false, ArrowDown: false, ArrowLeft: false, ArrowRight: false, shift: false };
        let currentSpeed = WALK_SPEED;
        
        // ----- TERROR SOUND -----
        let audioCtx = null;
        let terrorLoopSource = null;
        let terrorGain = null;
        let gunshotInterval = null;
        let soundAllowed = false;
        
        // ----- Celebration effects -----
        let celebrationActive = false;
        let celebrationTimer = null;
        let balloons = [];
        let victoryBuzzerPlayed = false;
        
        function initAudio() {
            if (audioCtx) return;
            try {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                terrorGain = audioCtx.createGain();
                terrorGain.gain.value = 0.45;
                terrorGain.connect(audioCtx.destination);
            } catch(e) { console.warn("Web Audio not supported"); }
        }
        
        function startTerrorLoop() {
            if (!audioCtx || !soundAllowed) return;
            try {
                if (terrorLoopSource) {
                    try { terrorLoopSource.stop(); } catch(e) {}
                }
                const bufferSize = audioCtx.sampleRate * 3;
                const buffer = audioCtx.createBuffer(1, bufferSize, audioCtx.sampleRate);
                const data = buffer.getChannelData(0);
                for (let i = 0; i < bufferSize; i++) {
                    let t = i / audioCtx.sampleRate;
                    let lowFreq = Math.sin(t * 55) * 0.4;
                    let rumble = (Math.random() - 0.5) * 0.25;
                    let swell = Math.sin(t * 0.8) * 0.2;
                    data[i] = (lowFreq + rumble + swell) * 0.7;
                }
                terrorLoopSource = audioCtx.createBufferSource();
                terrorLoopSource.buffer = buffer;
                terrorLoopSource.loop = true;
                terrorLoopSource.connect(terrorGain);
                terrorLoopSource.start();
            } catch(e) { console.log("drone err", e); }
        }
        
        function playRandomGunshot() {
            if (!audioCtx || !soundAllowed || !gameActive || gameWin || gameOverFlag) return;
            if (Math.random() > 0.38) return;
            try {
                const now = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.value = 120 + Math.random() * 80;
                gain.gain.value = 0.2;
                gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.5);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(now + 0.4);
                const noise = audioCtx.createBufferSource();
                const noiseBuffer = audioCtx.createBuffer(1, 2000, audioCtx.sampleRate);
                const noiseData = noiseBuffer.getChannelData(0);
                for (let i=0; i<2000; i++) noiseData[i] = (Math.random() - 0.5)*0.8;
                noise.buffer = noiseBuffer;
                const noiseGain = audioCtx.createGain();
                noiseGain.gain.value = 0.12;
                noise.connect(noiseGain);
                noiseGain.connect(audioCtx.destination);
                noise.start();
                noise.stop(now + 0.2);
            } catch(e) {}
        }
        
        function startTerrorSoundtrack() {
            if (!audioCtx) initAudio();
            if (!audioCtx || !soundAllowed) return;
            audioCtx.resume().then(() => {
                startTerrorLoop();
                if (gunshotInterval) clearInterval(gunshotInterval);
                gunshotInterval = setInterval(() => { playRandomGunshot(); }, 1800);
            }).catch(e=>console.log);
        }
        
        function stopTerrorSoundtrack() {
            if (gunshotInterval) { clearInterval(gunshotInterval); gunshotInterval = null; }
            if (terrorLoopSource) {
                try { terrorLoopSource.stop(); } catch(e) {}
                terrorLoopSource = null;
            }
        }
        
        function playVictoryBuzzer() {
            if (!audioCtx || victoryBuzzerPlayed) return;
            victoryBuzzerPlayed = true;
            try {
                const now = audioCtx.currentTime;
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.value = 880;
                gain.gain.value = 0.5;
                gain.gain.exponentialRampToValueAtTime(0.001, now + 1.5);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(now + 1.5);
                
                const osc2 = audioCtx.createOscillator();
                osc2.type = 'sine';
                osc2.frequency.value = 440;
                osc2.connect(gain);
                osc2.start();
                osc2.stop(now + 1.5);
            } catch(e) { console.log("buzzer err", e); }
        }
        
        function startCelebration() {
            if (celebrationActive) return;
            celebrationActive = true;
            victoryBuzzerPlayed = false;
            playVictoryBuzzer();
            balloons = [];
            for (let i = 0; i < 50; i++) {
                balloons.push({
                    x: Math.random() * W,
                    y: H + Math.random() * 100,
                    radius: 10 + Math.random() * 15,
                    color: Math.random() > 0.5 ? "#00209f" : "#d21034",
                    speed: 1 + Math.random() * 2,
                    angle: Math.random() * Math.PI * 2
                });
            }
            if (celebrationTimer) clearTimeout(celebrationTimer);
            celebrationTimer = setTimeout(() => {
                celebrationActive = false;
                balloons = [];
            }, 5000);
        }
        
        function drawCelebration() {
            if (!celebrationActive) return;
            for (let b of balloons) {
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
                ctx.fillStyle = b.color;
                ctx.fill();
                ctx.fillStyle = "gold";
                ctx.font = `${b.radius}px monospace`;
                ctx.fillText("🎈", b.x - b.radius/2, b.y - b.radius/2);
                b.y -= b.speed;
                if (b.y + b.radius < 0) {
                    b.y = H + b.radius;
                    b.x = Math.random() * W;
                }
            }
        }
        
        // ---- reset & gameplay functions ----
        function fullGameReset() {
            gameActive = true;
            gameWin = false;
            gameOverFlag = false;
            celebrationActive = false;
            balloons = [];
            if (celebrationTimer) clearTimeout(celebrationTimer);
            statusSpan.innerText = "🏃‍♂️ ESCAPE! AVOID BULLETS 🏃‍♂️";
            statusSpan.style.color = "#f7d44a";
            father.x = 90;
            father.y = H/2;
            updateSonsPosition(true);
            bullets = [];
            for (let e of enemies) {
                e.cooldown = Math.floor(Math.random() * 30);
            }
            currentSpeed = WALK_SPEED;
            if (autoRestartTimeout) clearTimeout(autoRestartTimeout);
            autoRestartTimeout = null;
        }
        
        function updateSonsPosition(forceDirect=false) {
            for (let i = 0; i < sons.length; i++) {
                let targetX = father.x + sons[i].offsetX;
                let targetY = father.y + sons[i].offsetY;
                if (forceDirect) {
                    sons[i].x = targetX;
                    sons[i].y = targetY;
                } else {
                    sons[i].x += (targetX - sons[i].x) * 0.28;
                    sons[i].y += (targetY - sons[i].y) * 0.28;
                }
                sons[i].x = Math.min(W - SON_RADIUS - 2, Math.max(SON_RADIUS + 2, sons[i].x));
                sons[i].y = Math.min(H - SON_RADIUS - 2, Math.max(SON_RADIUS + 2, sons[i].y));
            }
        }
        
        function checkBulletCollisions() {
            if (!gameActive) return false;
            const allChars = [father, ...sons];
            for (let i = bullets.length-1; i >= 0; i--) {
                const b = bullets[i];
                let hit = false;
                for (let char of allChars) {
                    const dx = b.x - char.x;
                    const dy = b.y - char.y;
                    const dist = Math.hypot(dx, dy);
                    if (dist < b.radius + char.radius) {
                        hit = true;
                        break;
                    }
                }
                if (hit) {
                    bullets.splice(i,1);
                    return true;
                }
            }
            return false;
        }
        
        // Enemies shoot at each other
        function enemyShoot(enemy) {
            if (!gameActive || gameWin) return;
            const otherEnemies = enemies.filter(e => e !== enemy);
            if (otherEnemies.length === 0) return;
            const target = otherEnemies[Math.floor(Math.random() * otherEnemies.length)];
            let angle = Math.atan2(target.y - enemy.y, target.x - enemy.x);
            angle += (Math.random() - 0.5) * 0.3;
            const speed = 5.2;
            const vx = Math.cos(angle) * speed;
            const vy = Math.sin(angle) * speed;
            bullets.push({
                x: enemy.x, y: enemy.y, radius: BULLET_RADIUS,
                vx: vx, vy: vy
            });
        }
        
        function updateEnemiesShooting() {
            for (let e of enemies) {
                if (e.cooldown <= 0) {
                    enemyShoot(e);
                    e.cooldown = e.shootDelay + Math.floor(Math.random() * 25);
                } else {
                    e.cooldown--;
                }
            }
        }
        
        function updateBullets() {
            for (let i=0; i<bullets.length; i++) {
                bullets[i].x += bullets[i].vx;
                bullets[i].y += bullets[i].vy;
                if (bullets[i].x < -50 || bullets[i].x > W+50 || bullets[i].y < -50 || bullets[i].y > H+50) {
                    bullets.splice(i,1);
                    i--;
                }
            }
        }
        
        function handleMovement() {
            if (!gameActive) return;
            let speed = keys.shift ? RUN_SPEED : WALK_SPEED;
            currentSpeed = speed;
            let moveX = 0, moveY = 0;
            if (keys.ArrowUp) moveY -= 1;
            if (keys.ArrowDown) moveY += 1;
            if (keys.ArrowLeft) moveX -= 1;
            if (keys.ArrowRight) moveX += 1;
            if (moveX !== 0 || moveY !== 0) {
                const len = Math.hypot(moveX, moveY);
                moveX = moveX/len * speed;
                moveY = moveY/len * speed;
            }
            let newX = father.x + moveX;
            let newY = father.y + moveY;
            father.x = Math.min(W - FATHER_RADIUS - 5, Math.max(FATHER_RADIUS + 5, newX));
            father.y = Math.min(H - FATHER_RADIUS - 5, Math.max(FATHER_RADIUS + 5, newY));
        }
        
        function checkWin() {
            if (!gameActive || gameWin) return false;
            let fatherSafe = (father.x + FATHER_RADIUS > SAFE_ZONE_X && father.y > SAFE_ZONE_Y_MIN && father.y < SAFE_ZONE_Y_MAX);
            let sonsSafe = sons.every(s => (s.x + SON_RADIUS > SAFE_ZONE_X && s.y > SAFE_ZONE_Y_MIN && s.y < SAFE_ZONE_Y_MAX));
            if (fatherSafe && sonsSafe && gameActive) {
                gameActive = false;
                gameWin = true;
                statusSpan.innerText = "🌟 VICTORY! SAFE REFUGE 🌟";
                statusSpan.style.color = "#adff2f";
                stopTerrorSoundtrack();
                startCelebration();
                return true;
            }
            return false;
        }
        
        function triggerGameOver() {
            if (!gameActive) return;
            gameActive = false;
            gameOverFlag = true;
            statusSpan.innerText = "💀 GAME OVER... Restarting 💀";
            statusSpan.style.color = "#ff5555";
            stopTerrorSoundtrack();
            celebrationActive = false;
            if (celebrationTimer) clearTimeout(celebrationTimer);
            if (autoRestartTimeout) clearTimeout(autoRestartTimeout);
            autoRestartTimeout = setTimeout(() => {
                // Reset the game
                fullGameReset();
                // Restart sound
                soundAllowed = true;
                if (audioCtx) {
                    audioCtx.resume().then(() => {
                        startTerrorSoundtrack();
                    }).catch(()=>{});
                } else {
                    startTerrorSoundtrack();
                }
                statusSpan.innerText = "🏃‍♂️ ESCAPE! AVOID BULLETS 🏃‍♂️";
                statusSpan.style.color = "#f7d44a";
                autoRestartTimeout = null;
            }, 2000);
        }
        
        // Drawing functions
        function drawBackgroundGhetto() {
            ctx.fillStyle = "#1f2a2e";
            ctx.fillRect(0,0,W,H);
            ctx.fillStyle = "#3a2c2b";
            for (let i=0;i<12;i++) {
                ctx.fillRect(40+i*90, H-140, 45, 130);
                ctx.fillStyle = "#5e4b3c";
                ctx.fillRect(30+i*95, H-190, 40, 50);
                ctx.fillStyle = "#2a211f";
            }
            ctx.fillStyle = "#6f4e2e";
            for(let i=0;i<20;i++) ctx.fillRect(20+i*55, H-70, 25, 65);
            ctx.fillStyle = "#543a28";
            for(let i=0;i<15;i++) ctx.fillRect(15+i*70, H-220, 30, 85);
            ctx.fillStyle = "#53412e";
            for(let i=0;i<30;i++) ctx.fillRect(20+i*33, H-45, 6, 8);
            ctx.fillStyle = "#7d5d42";
            for(let i=0;i<12;i++) ctx.beginPath(), ctx.arc(70+i*100, H-100, 8,0,Math.PI*2), ctx.fill();
            ctx.font = "bold 20px monospace";
            ctx.fillStyle = "#9e7b5c66";
            ctx.fillText("LARI KOZE", 500, 350);
            ctx.fillStyle = "#c98f5e66";
            ctx.fillText("CHAPO!", 760, 520);
        }
        
        function drawEnemies() {
            for (let e of enemies) {
                ctx.shadowBlur = 0;
                if (e.type === "bandit") {
                    ctx.fillStyle = "#1b2b1f";
                    ctx.beginPath();
                    ctx.arc(e.x, e.y, 14, 0, Math.PI*2);
                    ctx.fill();
                    ctx.fillStyle = "#bc9a6c";
                    ctx.fillRect(e.x-8, e.y-4, 16, 6);
                    ctx.fillStyle = "#7a2e2e";
                    ctx.beginPath();
                    ctx.moveTo(e.x+10, e.y-2);
                    ctx.lineTo(e.x+18, e.y-8);
                    ctx.lineTo(e.x+14, e.y+2);
                    ctx.fill();
                } else {
                    ctx.fillStyle = "#2c4763";
                    ctx.beginPath();
                    ctx.arc(e.x, e.y, 14, 0, Math.PI*2);
                    ctx.fill();
                    ctx.fillStyle = "#27466e";
                    ctx.fillRect(e.x-7, e.y-5, 14, 8);
                    ctx.fillStyle = "#c97e3a";
                    ctx.beginPath();
                    ctx.rect(e.x-4, e.y-12, 8, 6);
                    ctx.fill();
                }
                ctx.fillStyle = "#000000";
                ctx.beginPath();
                ctx.arc(e.x-5, e.y-3, 2, 0, Math.PI*2);
                ctx.arc(e.x+5, e.y-3, 2, 0, Math.PI*2);
                ctx.fill();
            }
        }
        
        function drawBullets() {
            for (let b of bullets) {
                ctx.fillStyle = "#ffaa33";
                ctx.shadowBlur = 8;
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.radius-2, 0, Math.PI*2);
                ctx.fill();
                ctx.fillStyle = "#ff4500";
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.radius-4, 0, Math.PI*2);
                ctx.fill();
            }
            ctx.shadowBlur = 0;
        }
        
        function drawCharacters() {
            ctx.shadowBlur = 3;
            ctx.fillStyle = "#2b5797";
            ctx.beginPath();
            ctx.arc(father.x, father.y, FATHER_RADIUS, 0, Math.PI*2);
            ctx.fill();
            ctx.fillStyle = "#ffdb7e";
            ctx.beginPath();
            ctx.arc(father.x-4, father.y-4, 3, 0, Math.PI*2);
            ctx.arc(father.x+4, father.y-4, 3, 0, Math.PI*2);
            ctx.fill();
            ctx.fillStyle = "#6b3e1c";
            ctx.fillRect(father.x-6, father.y+3, 12, 5);
            const colors = ["#4f7e3e", "#cb7429", "#3f729b"];
            for (let i=0;i<sons.length;i++) {
                ctx.fillStyle = colors[i%3];
                ctx.beginPath();
                ctx.arc(sons[i].x, sons[i].y, SON_RADIUS, 0, Math.PI*2);
                ctx.fill();
                ctx.fillStyle = "#fce5b4";
                ctx.beginPath();
                ctx.arc(sons[i].x-3, sons[i].y-3, 2.2, 0, Math.PI*2);
                ctx.arc(sons[i].x+3, sons[i].y-3, 2.2, 0, Math.PI*2);
                ctx.fill();
            }
        }
        
        function drawSafeZone() {
            ctx.fillStyle = "#2c6e2ccc";
            ctx.shadowBlur = 0;
            ctx.fillRect(SAFE_ZONE_X-5, SAFE_ZONE_Y_MIN-10, W-SAFE_ZONE_X+10, SAFE_ZONE_Y_MAX-SAFE_ZONE_Y_MIN+20);
            ctx.fillStyle = "#edc531";
            ctx.font = "bold 20px monospace";
            ctx.fillText("🏠 SAFE HAVEN 🏠", SAFE_ZONE_X+15, SAFE_ZONE_Y_MIN+35);
            ctx.fillStyle = "#ffe5a3";
            ctx.font = "italic 14px monospace";
            ctx.fillText("LIBETE", SAFE_ZONE_X+55, SAFE_ZONE_Y_MAX-15);
        }
        
        function drawHUD() {
            ctx.font = "bold 14px 'Courier New'";
            ctx.fillStyle = "#ffd966";
            ctx.shadowBlur = 0;
            ctx.fillText(`🏃 SPEED: ${keys.shift ? "RUNNING" : "WALK"}`, 20, 40);
        }
        
        function gameUpdate() {
            if (gameContainer.style.display !== 'flex') return;
            if (gameActive && !gameWin && !gameOverFlag) {
                handleMovement();
                updateSonsPosition(false);
                updateEnemiesShooting();
                updateBullets();
                const gotHit = checkBulletCollisions();
                if (gotHit) triggerGameOver();
                else checkWin();
            }
            drawBackgroundGhetto();
            drawSafeZone();
            drawEnemies();
            drawBullets();
            drawCharacters();
            drawHUD();
            drawCelebration();
            if(gameActive && !gameWin && !gameOverFlag && Math.random()<0.1){
                ctx.fillStyle = "#ffaa3344";
                ctx.fillRect(0,0,W,H);
            }
        }
        
        function animate() {
            gameUpdate();
            animationId = requestAnimationFrame(animate);
        }
        
        function launchGame() {
            fullGameReset();
            gameActive = true;
            gameWin = false;
            gameOverFlag = false;
            bullets = [];
            updateSonsPosition(true);
            soundAllowed = true;
            if (!audioCtx) initAudio();
            if (audioCtx) {
                audioCtx.resume().then(() => {
                    startTerrorSoundtrack();
                }).catch(()=>{});
            } else {
                startTerrorSoundtrack();
            }
            statusSpan.innerText = "🏃‍♂️ ESCAPE! AVOID BULLETS 🏃‍♂️";
            statusSpan.style.color = "#f7d44a";
        }
        
        function logout() {
            stopTerrorSoundtrack();
            soundAllowed = false;
            gameActive = false;
            gameWin = false;
            gameOverFlag = false;
            celebrationActive = false;
            if (celebrationTimer) clearTimeout(celebrationTimer);
            if (autoRestartTimeout) clearTimeout(autoRestartTimeout);
            autoRestartTimeout = null;
            gameContainer.style.display = 'none';
            startScreenDiv.style.display = 'flex';
            passwordInput.value = '';
            passwordError.style.display = 'none';
            keys.ArrowUp = false;
            keys.ArrowDown = false;
            keys.ArrowLeft = false;
            keys.ArrowRight = false;
            keys.shift = false;
            generateStars();
        }
        
        // Touch and keyboard controls
        function simulateKey(key, isDown) {
            if (key === 'Shift') {
                keys.shift = isDown;
            } else if (key === 'ArrowUp' || key === 'ArrowDown' || key === 'ArrowLeft' || key === 'ArrowRight') {
                keys[key] = isDown;
            }
            if (isDown) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        }
        
        function initTouchControls() {
            const touchButtons = document.querySelectorAll('.touch-btn');
            touchButtons.forEach(btn => {
                const key = btn.getAttribute('data-key');
                if (!key) return;
                btn.addEventListener('touchstart', (e) => {
                    e.preventDefault();
                    simulateKey(key, true);
                });
                btn.addEventListener('touchend', (e) => {
                    e.preventDefault();
                    simulateKey(key, false);
                });
                btn.addEventListener('touchcancel', (e) => {
                    e.preventDefault();
                    simulateKey(key, false);
                });
                btn.addEventListener('mousedown', (e) => {
                    e.preventDefault();
                    simulateKey(key, true);
                });
                btn.addEventListener('mouseup', (e) => {
                    e.preventDefault();
                    simulateKey(key, false);
                });
                btn.addEventListener('mouseleave', (e) => {
                    simulateKey(key, false);
                });
            });
        }
        
        function initKeyboard() {
            window.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowUp' || e.key === 'ArrowDown' || e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
                    e.preventDefault();
                    keys[e.key] = true;
                }
                if (e.key === 'Shift') {
                    keys.shift = true;
                    e.preventDefault();
                }
                if (e.key === 'r' || e.key === 'R') {
                    if (gameContainer.style.display === 'flex' && (!gameActive || gameWin || gameOverFlag)) {
                        // manual restart – cancel auto restart and reset
                        if (autoRestartTimeout) clearTimeout(autoRestartTimeout);
                        fullGameReset();
                        gameActive = true;
                        gameWin = false;
                        gameOverFlag = false;
                        stopTerrorSoundtrack();
                        startTerrorSoundtrack();
                        bullets = [];
                        for(let e of enemies) e.cooldown = 5;
                        updateSonsPosition(true);
                    }
                }
            });
            window.addEventListener('keyup', (e) => {
                if (e.key === 'ArrowUp' || e.key === 'ArrowDown' || e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
                    keys[e.key] = false;
                }
                if (e.key === 'Shift') keys.shift = false;
            });
        }
        
        function generateStars() {
            const starsDiv = document.getElementById('starsField');
            starsDiv.innerHTML = '';
            for (let i=0;i<65;i++) {
                const star = document.createElement('div');
                star.classList.add('star');
                const size = 3+Math.random()*7;
                star.style.width = size+'px';
                star.style.height = size+'px';
                star.style.left = Math.random()*100+'%';
                star.style.top = Math.random()*100+'%';
                star.style.animationDelay = Math.random()*2+'s';
                star.style.animationDuration = 1+Math.random()*2+'s';
                starsDiv.appendChild(star);
            }
        }
        
        // Fullscreen toggle
        function toggleFullscreen() {
            const elem = document.documentElement;
            if (!document.fullscreenElement) {
                elem.requestFullscreen().catch(err => {
                    console.warn(`Fullscreen error: ${err.message}`);
                });
                fullscreenBtn.textContent = "✖ EXIT";
            } else {
                document.exitFullscreen();
                fullscreenBtn.textContent = "⛶ FULLSCREEN";
            }
        }
        
        document.addEventListener('fullscreenchange', () => {
            if (document.fullscreenElement) {
                fullscreenBtn.textContent = "✖ EXIT";
            } else {
                fullscreenBtn.textContent = "⛶ FULLSCREEN";
            }
        });
        
        fullscreenBtn.addEventListener('click', toggleFullscreen);
        
        // Password check
        startBtn.addEventListener('click', () => {
            const password = passwordInput.value.trim();
            if (password === "20082010") {
                passwordError.style.display = "none";
                generateStars();
                startScreenDiv.style.display = 'none';
                gameContainer.style.display = 'flex';
                launchGame();
                initTouchControls();
                if (!animationId) animate();
            } else {
                passwordError.style.display = "block";
                passwordInput.value = "";
                passwordInput.focus();
            }
        });
        
        resetBtn.addEventListener('click', () => {
            if (gameContainer.style.display === 'flex') {
                if (autoRestartTimeout) clearTimeout(autoRestartTimeout);
                fullGameReset();
                gameActive = true;
                gameWin = false;
                gameOverFlag = false;
                stopTerrorSoundtrack();
                startTerrorSoundtrack();
                bullets = [];
                for(let e of enemies) e.cooldown = 5;
                updateSonsPosition(true);
            }
        });
        
        logoutBtn.addEventListener('click', () => {
            logout();
        });
        
        generateStars();
        initKeyboard();
        animate();
    })();
</script>
</body>
</html>
"""

st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-top: -20px;">
        <div style="max-width: 1020px; width: 100%; overflow-x: auto;">
    """,
    unsafe_allow_html=True
)

st.components.v1.html(GAME_HTML, height=720, scrolling=False)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown(
    """
    ---
    ### 🎮 Game Controls
    - **Keyboard:** Arrow keys to move, SHIFT to run.
    - **Touch:** Tap the on‑screen buttons (▲◀▼▶) to move, and tap **RUN** to sprint.
    - **Goal:** Bring the whole family into the green **Safe Haven** on the right side of the screen.
    - Avoid bullets fired by bandits and police. One hit ends the round, and the game automatically restarts.
    """
)
