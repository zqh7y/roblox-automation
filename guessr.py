# ===========================================
# ROBLOX AUTOMATION - TRIPLE CLICK SELECT ⚡
# ===========================================
# 1st input: (346, 448)
# 2nd input: (345, 516)
# Button:    (480, 584)
# Extra pre‑button triple clicks: (630, 448) and (630, 516)
# ===========================================

import sys
import time
import pyautogui
import pygetwindow as gw
from algo import generate_candidates

# Auto-install missing packages
try:
    import pyautogui
except ImportError:
    print("[INSTALL] Installing pyautogui...")
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    import pyautogui

try:
    import pygetwindow as gw
except ImportError:
    print("[INSTALL] Installing pygetwindow...")
    import subprocess

    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygetwindow"])
    import pygetwindow as gw

# ⚡ ZERO DELAY MODE for inputs ⚡
pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0
pyautogui.FAILSAFE = True


def focus_vscode_terminal():
    """Find and focus the VS Code terminal window"""
    print("\n   🔄 Switching focus to VS Code terminal...")
    vscode_windows = []
    for window in gw.getAllWindows():
        title = window.title
        if title and (
            "Visual Studio Code" in title
            or "Code" in title
            or "powershell" in title.lower()
            or "terminal" in title.lower()
        ):
            vscode_windows.append(window)

    if vscode_windows:
        vscode_windows[0].activate()
        time.sleep(0.05)
        print("   ✅ VS Code terminal focused")
        return True
    else:
        print("   ⚠️ VS Code window not found, trying Alt+Tab...")
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.05)
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.05)
        return False


def select_all_triple_click():
    """Triple‑click to select all text in the field (turbo)"""
    pyautogui.click()
    time.sleep(0.03)
    pyautogui.click()
    time.sleep(0.03)
    pyautogui.click()
    time.sleep(0.05)


def triple_click_at(pos):
    """Triple‑click at a given position with tiny delays."""
    pyautogui.moveTo(pos[0], pos[1], duration=0)
    time.sleep(0.02)
    pyautogui.click()
    time.sleep(0.03)
    pyautogui.click()
    time.sleep(0.03)
    pyautogui.click()
    time.sleep(0.05)


def click_button_reliable():
    """
    - Instant move to button (480,584)
    - Click once
    - Move 10px right to (490,584) over 0.5s
    - Click again
    """
    print("   🖱️ Instant move to button...")
    pyautogui.moveTo(pos3[0], pos3[1], duration=0)
    time.sleep(0.05)
    pyautogui.click()
    print("   ✅ First click")

    # Move 10px right over 0.5 seconds
    target_x = pos3[0] + 10
    target_y = pos3[1]
    print(f"   ➡️ Moving to ({target_x}, {target_y}) over 0.5s...")
    pyautogui.moveTo(target_x, target_y, duration=0.5)
    time.sleep(0.05)
    pyautogui.click()
    print("   ✅ Second click (after move)")


def main():
    print("=" * 60)
    print("     ROBLOX AUTOMATION - TRIPLE CLICK SELECT ⚡")
    print("=" * 60)

    # HARDCODED POSITIONS
    global pos3
    pos1 = (346, 448)
    pos2 = (345, 516)
    pos3 = (480, 584)  # button
    extra1 = (630, 448)
    extra2 = (630, 516)

    print("\n📍 POSITIONS:")
    print(f"   Input 1: {pos1}")
    print(f"   Input 2: {pos2}")
    print(f"   Button:  {pos3} (instant + 10px right move)")
    print(f"   Extra 1: {extra1} (auto triple‑click + delete)")
    print(f"   Extra 2: {extra2} (auto triple‑click + delete)")

    # ============ STEP 1: FIRST INPUT ============
    print("\n" + "=" * 60)
    print("STEP 1: FIRST INPUT FIELD")
    print("=" * 60)

    print(f"\n📍 Moving mouse to first input at {pos1}...")
    pyautogui.moveTo(pos1[0], pos1[1], duration=0)
    time.sleep(0.05)

    confirm1 = (
        input("✅ Is this the correct FIRST input field? (y/n): ").strip().lower()
    )
    if confirm1 not in ("y", ""):
        print("❌ Automation cancelled at STEP 1")
        return

    print("\n   👆 Click BACK to terminal window now...")
    print("   (Then press Enter when ready to continue)")
    input()

    print("\n📝 Text for FIRST input field")
    raw = input("Enter text for first field: ")
    text1 = raw.rstrip()

    # Generate all possible second‑input candidates (filtered to length >=8)
    candidates = generate_candidates(text1)
    print(f"\n🤖 Found {len(candidates)} possible outputs (length >=8):")
    for i, cand in enumerate(candidates, 1):
        print(f"   {i}. {cand}")

    # ---------- AUTOMATIC PROCESSING OF EACH CANDIDATE ----------
    for idx, text2 in enumerate(candidates, 1):
        print(f"\n{'='*60}")
        print(f"PROCESSING CANDIDATE #{idx}: '{text2}'")
        print(f"{'='*60}")

        # Focus Roblox for the second input
        print("\n   🔄 Focusing Roblox...")
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.05)

        # Move to second input position and fill it
        print(f"\n📍 Moving mouse to second input at {pos2}...")
        pyautogui.moveTo(pos2[0], pos2[1], duration=0)
        time.sleep(0.05)

        # Clear and type the second input
        select_all_triple_click()
        pyautogui.press("delete")
        time.sleep(0.05)
        pyautogui.write(text2, interval=0)
        time.sleep(0.05)
        print(f"   ✅ Entered: '{text2}' at {pos2}")

        # ---------- AUTOMATIC PRE-BUTTON ACTIONS ----------
        print("\n" + "-" * 40)
        print("AUTOMATIC PRE-BUTTON ACTIONS")
        print("-" * 40)

        # First extra position
        print(f"📍 Triple‑clicking at extra1 {extra1}...")
        triple_click_at(extra1)
        pyautogui.press("delete")
        time.sleep(0.05)
        print("   ✅ Extra1 triple‑clicked + delete")

        # Second extra position
        print(f"📍 Triple‑clicking at extra2 {extra2}...")
        triple_click_at(extra2)
        pyautogui.press("delete")
        time.sleep(0.05)
        print("   ✅ Extra2 triple‑clicked + delete")

        # ---------- BUTTON CLICK (AUTOMATIC) ----------
        print("\n" + "-" * 40)
        print("CLICKING BUTTON")
        print("-" * 40)

        click_button_reliable()

        # 👇 3‑second pause after button click before next candidate
        print("   ⏸️ Waiting 3 seconds...")
        time.sleep(3)

    # ============ ALL CANDIDATES COMPLETED ============
    focus_vscode_terminal()
    print("\n" + "=" * 60)
    print("✅✅✅ ALL CANDIDATES PROCESSED! ✅✅✅")
    print("=" * 60)
    print(f"\n📋 SUMMARY:")
    print(f"   First input:  '{text1}'")
    print(f"   Candidates processed: {len(candidates)}")
    for i, cand in enumerate(candidates, 1):
        print(f"      #{i}: '{cand}'")
    print("\n" + "=" * 60)

    again = input("\nRun again with a new first input? (y/n): ").strip().lower()
    if again in ("y", ""):
        main()
    else:
        print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()
