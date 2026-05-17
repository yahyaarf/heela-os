# MEMORY_IMAGE_FILES = [
#     Path("/Users/macbookair/Desktop/heela app/berg.jpg"),
#     Path("/Users/macbookair/Desktop/heela app/Osama_bin_Laden.jpg"),
#     Path("/Users/macbookair/Desktop/heela app/Screenshot_2026-05-17_at_10.34.23_PM-removebg-preview.png"),
#     Path("/Users/macbookair/Desktop/heela app/test3.jpg"),
# ]

import json
import base64
from datetime import datetime
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="Heela OS",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Main profile picture top-left
PROFILE_IMAGE_FILE = Path("/assets/profile.jpg")

# Finder / Memories pictures — replace these 4 paths with your real picture paths

MEMORY_IMAGE_FILES = [
    Path("memory1.jpg"),
    Path("memory2.jpg"),
    Path("memory3.jpg"),
    Path("profile.png"),
]


# =====================================================
# HELPERS
# =====================================================
def img_base64(path):
    if not path.exists():
        return None
    return base64.b64encode(path.read_bytes()).decode()


def build_memory_gallery():
    cards = ""
    for index, img_path in enumerate(MEMORY_IMAGE_FILES, start=1):
        img_b64 = img_base64(img_path)
        if img_b64:
            cards += f"""
                <div class="memory-card">
                    <img src="data:image/png;base64,{img_b64}" alt="memory {index}" />
                    <div class="memory-caption">Memory {index}</div>
                </div>
            """
        else:
            cards += f"""
                <div class="memory-card empty-memory">
                    <div>Missing<br>Memory {index}</div>
                    <small>{img_path.name}</small>
                </div>
            """

    return f"""
        <div class="memory-grid">
            {cards}
        </div>
    """


# =====================================================
# SIDEBAR — ONLY FOR UPLOADING HER PIC
# =====================================================
with st.sidebar:
    st.title("Heela OS Settings")
    st.caption("Upload her picture here, then close the sidebar.")

    uploaded = st.file_uploader("Upload her picture", type=["png", "jpg", "jpeg", "webp"])
    if uploaded is not None:
        PROFILE_IMAGE_FILE.write_bytes(uploaded.getvalue())
        st.success("Picture saved. Close sidebar to see it.")


# =====================================================
# STREAMLIT PAGE CLEANUP
# =====================================================
st.markdown(
    """
    <style>
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        margin: 0 !important;
        padding: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow: hidden !important;
        background: #111827 !important;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"], .stDeployButton,
    button[kind="header"] {
        display: none !important;
    }

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100vw !important;
        height: 100vh !important;
        overflow: hidden !important;
    }

    iframe {
        display: block !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =====================================================
# PROFILE IMAGE
# =====================================================
photo_b64 = img_base64(PROFILE_IMAGE_FILE)
if photo_b64:
    photo_html = f"<img src='data:image/png;base64,{photo_b64}' alt='heela profile' />"
else:
    photo_html = "<div class='upload-text'>Upload<br>her pic<br>from sidebar</div>"

memory_gallery_html = build_memory_gallery()
current_time = datetime.now().strftime("%a %I:%M %p")


# =====================================================
# FULL FIXED HTML/CSS/JS MINI MACOS
# =====================================================
html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
    * {{
        box-sizing: border-box;
        user-select: none;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", sans-serif;
    }}

    body {{
        background:
            radial-gradient(circle at 15% 22%, rgba(255,255,255,0.82), rgba(255,255,255,0.08) 28%, transparent 47%),
            radial-gradient(circle at 86% 18%, rgba(0,118,255,0.58), rgba(0,118,255,0.16) 34%, transparent 55%),
            radial-gradient(circle at 72% 84%, rgba(255,138,184,0.44), transparent 46%),
            linear-gradient(135deg, #80b8d8 0%, #d8e9ee 38%, #f3eadf 62%, #efc0d6 100%);
    }}

    .desktop {{
        position: fixed;
        inset: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
    }}

    .topbar {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 30px;
        z-index: 100;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 14px;
        background: rgba(13, 34, 54, 0.24);
        color: rgba(255,255,255,0.96);
        backdrop-filter: blur(22px);
        box-shadow: 0 1px 0 rgba(255,255,255,0.18);
        font-size: 12px;
        font-weight: 760;
    }}

    .top-left, .top-right {{
        display: flex;
        align-items: center;
        gap: 16px;
        white-space: nowrap;
    }}

    .apple-dot {{
        width: 13px;
        height: 13px;
        border-radius: 4px;
        background: rgba(255,255,255,0.94);
    }}

    .profile {{
        position: absolute;
        top: 54px;
        left: 34px;
        width: 125px;
        text-align: center;
        z-index: 20;
    }}

    .profile-box {{
        width: 112px;
        height: 112px;
        margin: 0 auto 7px auto;
        border-radius: 24px;
        overflow: hidden;
        background: rgba(255,255,255,0.34);
        border: 1px solid rgba(255,255,255,0.62);
        backdrop-filter: blur(18px);
        box-shadow: 0 18px 42px rgba(24,51,84,0.18);
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .profile-box img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}

    .upload-text {{
        color: white;
        font-size: 12px;
        font-weight: 900;
        line-height: 1.35;
        text-shadow: 0 2px 8px rgba(0,0,0,0.22);
    }}

    .label {{
        display: inline-block;
        max-width: 122px;
        padding: 3px 8px;
        border-radius: 8px;
        background: rgba(19,32,47,0.28);
        color: white;
        font-size: 12px;
        font-weight: 820;
        text-shadow: 0 1px 4px rgba(0,0,0,0.26);
    }}

    .right-folders {{
        position: absolute;
        top: 58px;
        right: 34px;
        width: 118px;
        z-index: 25;
    }}

    .folder {{
        width: 118px;
        text-align: center;
        margin-bottom: 23px;
        color: white;
        cursor: pointer;
    }}

    .folder-icon {{
        position: relative;
        width: 92px;
        height: 74px;
        margin: 0 auto 6px auto;
        border-radius: 17px;
        background: linear-gradient(145deg, #ffdc66, #f5a936);
        border: 1px solid rgba(255,255,255,0.58);
        box-shadow: 0 18px 34px rgba(48,67,92,0.18), inset 0 1px 0 rgba(255,255,255,0.55);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        transition: transform 0.15s ease;
    }}

    .folder:hover .folder-icon {{
        transform: translateY(-4px) scale(1.03);
    }}

    .folder-icon::before {{
        content: "";
        position: absolute;
        top: -9px;
        left: 11px;
        width: 38px;
        height: 17px;
        border-radius: 9px 9px 3px 3px;
        background: #ffdf76;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.55);
    }}

    .center-brand {{
        position: absolute;
        left: 50%;
        top: 40%;
        transform: translate(-50%, -50%);
        text-align: center;
        z-index: 5;
        pointer-events: none;
    }}

    .center-brand h1 {{
        margin: 0;
        font-size: clamp(92px, 13vw, 185px);
        line-height: 0.8;
        letter-spacing: -8px;
        color: rgba(255,255,255,0.54);
        text-shadow: 0 24px 76px rgba(27,60,91,0.20);
    }}

    .center-brand p {{
        color: rgba(255,255,255,0.84);
        font-size: 17px;
        font-weight: 800;
        margin-top: 18px;
        text-shadow: 0 2px 10px rgba(0,0,0,0.20);
    }}

    .window {{
        position: absolute;
        left: 50%;
        top: 52%;
        transform: translate(-50%, -50%);
        width: min(760px, 56vw);
        height: min(430px, 54vh);
        z-index: 40;
        border-radius: 18px;
        overflow: hidden;
        background: rgba(246,248,252,0.78);
        border: 1px solid rgba(255,255,255,0.72);
        backdrop-filter: blur(24px);
        box-shadow: 0 30px 90px rgba(28,52,78,0.24);
    }}

    .window-bar {{
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 13px;
        background: rgba(255,255,255,0.58);
        border-bottom: 1px solid rgba(255,255,255,0.65);
        color: rgba(35,39,47,0.75);
        font-size: 13px;
        font-weight: 900;
    }}

    .traffic {{
        display: flex;
        gap: 8px;
    }}

    .traffic span {{
        width: 12px;
        height: 12px;
        display: block;
        border-radius: 999px;
    }}

    .red {{ background: #ff5f57; }}
    .yellow {{ background: #febc2e; }}
    .green {{ background: #28c840; }}

    .window-body {{
        height: calc(100% - 38px);
        overflow-y: auto;
        padding: 22px;
        color: #252932;
    }}

    .window-body h2 {{
        margin: 0 0 10px 0;
        font-size: 32px;
        letter-spacing: -1.3px;
    }}

    .window-body p {{
        color: rgba(37,41,50,0.72);
        font-weight: 650;
        line-height: 1.5;
    }}

    .card {{
        border-radius: 16px;
        background: rgba(255,255,255,0.62);
        border: 1px solid rgba(255,255,255,0.75);
        padding: 18px;
        margin-bottom: 14px;
    }}

    .memory-grid {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;
        margin-top: 16px;
    }}

    .memory-card {{
        height: 145px;
        border-radius: 16px;
        overflow: hidden;
        position: relative;
        background: rgba(255,255,255,0.62);
        border: 1px solid rgba(255,255,255,0.78);
        box-shadow: 0 12px 28px rgba(34,60,90,0.10);
    }}

    .memory-card img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }}

    .memory-caption {{
        position: absolute;
        left: 10px;
        bottom: 10px;
        padding: 4px 9px;
        border-radius: 999px;
        background: rgba(17, 24, 39, 0.45);
        color: white;
        font-size: 12px;
        font-weight: 850;
        backdrop-filter: blur(12px);
    }}

    .empty-memory {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: rgba(37,41,50,0.62);
        font-weight: 900;
        gap: 8px;
    }}

    .empty-memory small {{
        font-size: 10px;
        opacity: 0.65;
        max-width: 90%;
        word-break: break-word;
    }}

    .message-mine {{
        background: linear-gradient(135deg, #007aff, #4e8dff);
        color: white;
        border-radius: 20px 20px 6px 20px;
        padding: 11px 14px;
        margin: 8px 0 8px auto;
        max-width: 72%;
        box-shadow: 0 10px 24px rgba(0,122,255,0.16);
    }}

    .message-other {{
        background: rgba(255,255,255,0.86);
        color: #282326;
        border-radius: 20px 20px 20px 6px;
        padding: 11px 14px;
        margin: 8px auto 8px 0;
        max-width: 72%;
        box-shadow: 0 10px 24px rgba(34,60,90,0.08);
    }}

    .message-name {{
        font-size: 11px;
        font-weight: 950;
        opacity: 0.70;
        margin-bottom: 4px;
    }}

    .message-time {{
        font-size: 10px;
        opacity: 0.60;
        margin-top: 5px;
    }}

    .chat-input {{
        display: flex;
        gap: 8px;
        margin-top: 12px;
    }}

    .chat-input input {{
        flex: 1;
        border: 0;
        outline: none;
        border-radius: 14px;
        padding: 12px 14px;
        background: rgba(255,255,255,0.86);
        font-size: 14px;
    }}

    .chat-input button {{
        border: 0;
        border-radius: 14px;
        padding: 0 16px;
        background: #007aff;
        color: white;
        font-weight: 900;
        cursor: pointer;
    }}

    .dock {{
        position: absolute;
        left: 50%;
        bottom: 18px;
        transform: translateX(-50%);
        z-index: 80;
        display: flex;
        align-items: end;
        gap: 12px;
        padding: 10px 14px;
        border-radius: 24px;
        background: rgba(255,255,255,0.38);
        border: 1px solid rgba(255,255,255,0.58);
        backdrop-filter: blur(28px);
        box-shadow: 0 22px 70px rgba(34,60,90,0.22);
    }}

    .dock button {{
        width: 62px;
        height: 62px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.75);
        background: rgba(255,255,255,0.70);
        box-shadow: 0 12px 28px rgba(34,60,90,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        cursor: pointer;
        transition: 0.15s ease;
    }}

    .dock button:hover {{
        transform: translateY(-8px) scale(1.05);
        background: rgba(255,255,255,0.92);
    }}

    @media (max-width: 1000px) {{
        .window {{ width: 68vw; }}
        .right-folders {{ transform: scale(0.88); transform-origin: top right; right: 16px; }}
        .profile {{ transform: scale(0.88); transform-origin: top left; left: 16px; }}
    }}
</style>
</head>
<body>
<div class="desktop">
    <div class="topbar">
        <div class="top-left">
            <div class="apple-dot"></div>
            <span>Finder</span>
            <span>File</span>
            <span>Edit</span>
            <span>View</span>
            <span>Go</span>
            <span>Window</span>
            <span>Help</span>
        </div>
        <div class="top-right">
            <span>Wi‑Fi</span>
            <span id="senderTop">Yahya</span>
            <span>{current_time}</span>
        </div>
    </div>

    <div class="profile">
        <div class="profile-box">{photo_html}</div>
        <div class="label">heela.profile</div>
    </div>

    <div class="right-folders">
        <div class="folder" onclick="openApp('finder')"><div class="folder-icon">📸</div><div class="label">Memories</div></div>
        <div class="folder" onclick="openApp('chat')"><div class="folder-icon">💬</div><div class="label">Chat</div></div>
        <div class="folder" onclick="openApp('moods')"><div class="folder-icon">✨</div><div class="label">Moods</div></div>
        <div class="folder" onclick="openApp('secrets')"><div class="folder-icon">🔐</div><div class="label">Secrets</div></div>
        <div class="folder" onclick="openApp('songs')"><div class="folder-icon">🎧</div><div class="label">Songs</div></div>
    </div>

    <div class="center-brand">
        <h1>heela</h1>
        <p>private desktop · made by Yahya</p>
    </div>

    <div class="window">
        <div class="window-bar">
            <div class="traffic"><span class="red"></span><span class="yellow"></span><span class="green"></span></div>
            <div id="windowTitle">Finder</div>
            <div style="width:52px"></div>
        </div>
        <div class="window-body" id="windowBody"></div>
    </div>

    <div class="dock">
        <button onclick="openApp('finder')" title="Finder">🗂️</button>
        <button onclick="openApp('chat')" title="Messages">💬</button>
        <button onclick="openApp('moods')" title="Moods">✨</button>
        <button onclick="openApp('secrets')" title="Secrets">🔐</button>
        <button onclick="openApp('songs')" title="Songs">🎧</button>
        <button onclick="openApp('finder')" title="Photo">🖼️</button>
        <button onclick="openApp('finder')" title="Trash">🗑️</button>
    </div>
</div>

<script>
    const pages = {{
        finder: {{
            title: "Finder — Memories",
            body: `
                <h2>Memories</h2>
                {memory_gallery_html}
            `
        }},
        moods: {{
            title: "Moods",
            body: `
                <h2>Moods</h2>
                <div class="card"><b>Sleepy Mode</b><br>System status: heela needs rest, tea, and zero unnecessary drama.</div>
                <div class="card"><b>Princess Mode</b><br>Priority level: very high. Handle with charm and snacks.</div>
                <div class="card"><b>Coffee Mode</b><br>Performance boost detected. Sass level may increase by 37%.</div>
            `
        }},
        secrets: {{
            title: "Secrets",
            body: `
                <h2>Secrets</h2>
                <p>Locked files. Password required.</p>

                <div class="card">
                    <b>Secret 1</b><br>
                    <button onclick="unlockSecret(1)">Open Secret 1</button>
                    <div id="secret-1" style="display:none; margin-top:12px;">You are officially the main character of this tiny OS.</div>
                </div>

                <div class="card">
                    <b>Secret 2</b><br>
                    <button onclick="unlockSecret(2)">Open Secret 2</button>
                    <div id="secret-2" style="display:none; margin-top:12px;">Warning: heela has dangerous levels of cuteness and should be handled carefully.</div>
                </div>

                <div class="card">
                    <b>Secret 3</b><br>
                    <button onclick="unlockSecret(3)">Open Secret 3</button>
                    <div id="secret-3" style="display:none; margin-top:12px;">I could have made something normal, but normal would not fit you.</div>
                </div>

                <div class="card">
                    <b>Secret 4</b><br>
                    <button onclick="unlockSecret(4)">Open Secret 4</button>
                    <div id="secret-4" style="display:none; margin-top:12px;">Final secret: this whole thing was just an excuse to make you smile.</div>
                </div>
            `
        }},
        songs: {{
            title: "Songs",
            body: `
                <h2>Songs</h2>
                <div class="card">Daniel Caesar — Best Part</div>
                <div class="card">SZA — Good Days</div>
                <div class="card">Dua Lipa — Levitating</div>
                <div class="card">Bruno Mars — Treasure</div>
            `
        }}
    }};

    function loadMessages() {{
        const saved = localStorage.getItem("heela_os_messages");
        if (saved) return JSON.parse(saved);
        return [
            {{ sender: "Yahya", text: "Welcome to Heela OS. This one finally looks normal.", time: "now" }}
        ];
    }}

    function saveMessages(messages) {{
        localStorage.setItem("heela_os_messages", JSON.stringify(messages));
    }}

    function renderChat() {{
        const messages = loadMessages();
        const bubbles = messages.map((m) => `
            <div class="${{m.sender === 'Yahya' ? 'message-mine' : 'message-other'}}">
                <div class="message-name">${{m.sender}}</div>
                <div>${{m.text}}</div>
                <div class="message-time">${{m.time}}</div>
            </div>
        `).join("");

        return `
            <h2>Messages</h2>
            <p>Choose sender, then type. This simple version stores chat in this browser.</p>
            <div class="card">
                <label><b>Sender:</b></label>
                <select id="senderSelect" onchange="document.getElementById('senderTop').textContent=this.value">
                    <option>Yahya</option>
                    <option>heela</option>
                </select>
            </div>
            <div id="chatBubbles">${{bubbles}}</div>
            <div class="chat-input">
                <input id="chatText" placeholder="Type something..." onkeydown="if(event.key==='Enter') sendMsg()" />
                <button onclick="sendMsg()">Send</button>
            </div>
        `;
    }}

    function sendMsg() {{
        const input = document.getElementById("chatText");
        const sender = document.getElementById("senderSelect").value;
        const text = input.value.trim();
        if (!text) return;
        const messages = loadMessages();
        const now = new Date().toLocaleTimeString([], {{hour: '2-digit', minute:'2-digit'}});
        messages.push({{ sender, text, time: now }});
        saveMessages(messages);
        openApp('chat');
    }}

    function unlockSecret(number) {{
        const passwords = {{
            1: "9090",
            2: "1022",
            3: "9845",
            4: "3480"
        }};

        const pass = prompt("Enter password for Secret " + number + ":");
        if (pass === passwords[number]) {{
            const secret = document.getElementById("secret-" + number);
            if (secret) secret.style.display = "block";
        }} else if (pass !== null) {{
            alert("Wrong password.");
        }}
    }}

    function openApp(app) {{
        const title = document.getElementById("windowTitle");
        const body = document.getElementById("windowBody");

        if (app === 'chat') {{
            title.textContent = "Messages";
            body.innerHTML = renderChat();
            setTimeout(() => {{
                const input = document.getElementById("chatText");
                if (input) input.focus();
            }}, 50);
            return;
        }}

        title.textContent = pages[app].title;
        body.innerHTML = pages[app].body;
    }}

    openApp('chat');
</script>
</body>
</html>
"""

components.html(html, height=900, scrolling=False)
