# ===========================================
# ROBLOX AUTOMATION - TRIPLE CLICK SELECT ⚡
# ===========================================
# 1st input: (346, 448)
# 2nd input: (345, 516)
# Button:    (471, 574)
# Extra pre‑button triple clicks: (630, 448) and (630, 516)
# ===========================================

import sys
import time
import pyautogui
import pygetwindow as gw
from algo import generate_candidates  # 👈 new import

# Auto-install missing packages (same as before)
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
    """Instant move, then two slow clicks (0.25s apart)"""
    print("   🖱️ Clicking button (instant move, slow clicks)...")
    pyautogui.moveTo(pos3[0], pos3[1], duration=0)  # ⚡ instant
    time.sleep(0.05)  # tiny safety
    pyautogui.click()  # first click
    time.sleep(0.25)  # 0.25s delay
    pyautogui.click()  # second click
    time.sleep(0.25)  # 0.25s delay
    print("   ✅ Button clicked twice (0.5s total)")


def main():
    print("=" * 60)
    print("     ROBLOX AUTOMATION - TRIPLE CLICK SELECT ⚡")
    print("=" * 60)

    # HARDCODED POSITIONS
    global pos3
    pos1 = (346, 448)
    pos2 = (345, 516)
    pos3 = (471, 574)
    extra1 = (630, 448)
    extra2 = (630, 516)

    print("\n📍 POSITIONS:")
    print(f"   Input 1: {pos1}")
    print(f"   Input 2: {pos2}")
    print(f"   Button:  {pos3}")
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

    # ============ CANDIDATE SELECTION ============
    candidates = generate_candidates(text1)
    if not candidates:
        # fallback, should never happen
        candidates = [text1 + "123"]

    print("\n🤖 Possible outputs:")
    for i, cand in enumerate(candidates, 1):
        print(f"   {i}. {cand}")

    if len(candidates) == 1:
        text2 = candidates[0]
        print(f"\n🤖 Auto-selected: '{text2}'")
    else:
        choice = input("\nChoose number (or press Enter for #1): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(candidates):
            text2 = candidates[int(choice) - 1]
        else:
            text2 = candidates[0]
        print(f"   Selected: '{text2}'")

    print("\n   👆 Click BACK to Roblox window now...")
    print("   (Press Enter when ready to type)")
    input()

    print(f"\n🚀 Filling first input...")
    pyautogui.moveTo(pos1[0], pos1[1], duration=0)
    time.sleep(0.05)
    select_all_triple_click()
    pyautogui.press("delete")
    time.sleep(0.05)
    pyautogui.write(text1, interval=0)
    time.sleep(0.05)
    print(f"   ✅ Entered: '{text1}' at {pos1}")
    time.sleep(0.05)

    # ============ STEP 2: SECOND INPUT ============
    print("\n" + "=" * 60)
    print("STEP 2: SECOND INPUT FIELD")
    print("=" * 60)

    focus_vscode_terminal()

    print(f"\n📍 Moving mouse to second input at {pos2}...")
    pyautogui.moveTo(pos2[0], pos2[1], duration=0)
    time.sleep(0.05)

    confirm2 = (
        input("✅ Is this the correct SECOND input field? (y/n): ").strip().lower()
    )
    if confirm2 not in ("y", ""):
        print("❌ Automation cancelled at STEP 2")
        return

    print("\n   👆 Click BACK to terminal window now...")
    print("   (Then press Enter when ready to continue)")
    input()

    print(f"\n📝 Using selected text: '{text2}'")

    print("\n   👆 Click BACK to Roblox window now...")
    print("   (Press Enter when ready to type)")
    input()

    print(f"\n🚀 Filling second input...")
    pyautogui.moveTo(pos2[0], pos2[1], duration=0)
    time.sleep(0.05)
    select_all_triple_click()
    pyautogui.press("delete")
    time.sleep(0.05)
    pyautogui.write(text2, interval=0)
    time.sleep(0.05)
    print(f"   ✅ Entered: '{text2}' at {pos2}")
    time.sleep(0.05)

    # ============ AUTOMATIC PRE-BUTTON ACTIONS ============
    print("\n" + "=" * 60)
    print("AUTOMATIC PRE-BUTTON ACTIONS")
    print("=" * 60)

    print("   🔄 Focusing Roblox for extra clicks...")
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.05)

    print(f"\n📍 Triple‑clicking at extra1 {extra1}...")
    triple_click_at(extra1)
    pyautogui.press("delete")
    time.sleep(0.05)
    print("   ✅ Extra1 triple‑clicked + delete")

    print(f"📍 Triple‑clicking at extra2 {extra2}...")
    triple_click_at(extra2)
    pyautogui.press("delete")
    time.sleep(0.05)
    print("   ✅ Extra2 triple‑clicked + delete")

    # ============ STEP 3: BUTTON ============
    print("\n" + "=" * 60)
    print("STEP 3: BUTTON")
    print("=" * 60)

    focus_vscode_terminal()

    print(f"\n📍 Moving mouse to button at {pos3}...")
    pyautogui.moveTo(pos3[0], pos3[1], duration=0)
    time.sleep(0.05)

    confirm3 = input("✅ Is this the correct BUTTON? (y/n): ").strip().lower()
    if confirm3 not in ("y", ""):
        print("❌ Automation cancelled at STEP 3")
        return

    print("\n   👆 Click BACK to Roblox window now...")
    print("   (Press Enter when ready to click)")
    input()

    click_button_reliable()
    focus_vscode_terminal()
    print("   🔄 Terminal refocused – ready for next steps.")

    # ============ COMPLETE ============
    print("\n" + "=" * 60)
    print("✅✅✅ AUTOMATION COMPLETE! ✅✅✅")
    print("=" * 60)
    print(f"\n📋 SUMMARY:")
    print(f"   Input 1: '{text1}' at {pos1}")
    print(f"   Input 2: '{text2}' at {pos2}")
    print(f"   Extra1:  triple‑clicked at {extra1}")
    print(f"   Extra2:  triple‑clicked at {extra2}")
    print(f"   Button:  clicked at {pos3}")
    print("\n" + "=" * 60)

    again = input("\nRun again? (y/n): ").strip().lower()
    if again in ("y", ""):
        main()
    else:
        print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()
