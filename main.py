from datetime import datetime

import gifos


def main():
    t = gifos.Terminal(750, 500, 15, 15)

    # ── BIOS boot ──
    t.toggle_show_cursor(False)
    year = datetime.now().strftime("%Y")
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    t.gen_text(
        f"Copyright (C) {year}, \x1b[31mtikket1 Systems Inc.\x1b[0m", 2
    )
    t.gen_text("\x1b[93mKrypton(tm) GIFCPU - 250Hz\x1b[0m", 4)

    for i in range(0, 65653, 7168):
        t.delete_row(6)
        t.gen_text(f"Memory Test: {i}", 6, contin=True)
    t.delete_row(6)
    t.gen_text("Memory Test: 64KB OK", 6, count=10, contin=True)
    t.gen_text("", 8, count=10, contin=True)

    # ── Login ──
    t.clear_frame()
    t.gen_text("\x1b[93mGIF OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("tikket1", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("**************", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now().strftime("%a %b %d %I:%M:%S %p %Y")
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    # ── Neofetch ──
    t.clear_frame()
    git_stats = gifos.utils.fetch_github_stats("tikket1")
    top_langs = [lang[0] for lang in git_stats.languages_sorted]

    t.gen_prompt(1, prompt="tikket1@kali")
    t.toggle_show_cursor(True)
    t.gen_typing_text(
        "\x1b[92mfetch.sh\x1b[0m \x1b[93m-u tikket1\x1b[0m", 1, contin=True
    )
    t.toggle_show_cursor(False)

    # ASCII art - small skull
    ascii_art = [
        "\x1b[37m    .-\"\"\"\"-.   \x1b[0m",
        "\x1b[37m   /        \\  \x1b[0m",
        "\x1b[37m  |  O    O  | \x1b[0m",
        "\x1b[37m  |  .----.  | \x1b[0m",
        "\x1b[37m  |  '----'  | \x1b[0m",
        "\x1b[37m   \\        /  \x1b[0m",
        "\x1b[37m    '------'   \x1b[0m",
        "\x1b[37m   /||    ||\\  \x1b[0m",
        "\x1b[37m  / ||    || \\ \x1b[0m",
    ]

    info_lines = [
        f"\x1b[97;1mtikket1\x1b[0m\x1b[37m@\x1b[0m\x1b[97;1mgithub\x1b[0m",
        "\x1b[37m─────────────────\x1b[0m",
        f"\x1b[96mRank:\x1b[0m      \x1b[93m{git_stats.user_rank.level}\x1b[0m",
        f"\x1b[96mStars:\x1b[0m     \x1b[93m{git_stats.total_stargazers}\x1b[0m",
        f"\x1b[96mCommits:\x1b[0m   \x1b[93m{git_stats.total_commits_last_year}\x1b[0m",
        f"\x1b[96mPRs:\x1b[0m       \x1b[93m{git_stats.total_pull_requests_made}\x1b[0m",
        f"\x1b[96mMerged:\x1b[0m    \x1b[93m{git_stats.pull_requests_merge_percentage}%\x1b[0m",
        f"\x1b[96mContribs:\x1b[0m  \x1b[93m{git_stats.total_repo_contributions}\x1b[0m",
        f"\x1b[96mLanguages:\x1b[0m \x1b[93m{', '.join(top_langs[:5])}\x1b[0m",
    ]

    row = 3
    max_lines = max(len(ascii_art), len(info_lines))
    for i in range(max_lines):
        art = ascii_art[i] if i < len(ascii_art) else "               "
        info = info_lines[i] if i < len(info_lines) else ""
        t.gen_text(f"{art}   {info}", row + i, count=2)

    row = row + max_lines + 1

    # Color blocks
    colors = ""
    for c in [31, 32, 33, 34, 35, 36, 37, 90]:
        colors += f"\x1b[{c}m\u2588\u2588\x1b[0m"
    t.gen_text(f"               {colors}", row, count=3)

    row += 2
    t.gen_prompt(row, prompt="tikket1@kali")
    t.toggle_show_cursor(True)
    t.gen_typing_text(
        "\x1b[92m# offensive security tooling\x1b[0m", row, contin=True
    )

    row += 1
    t.gen_prompt(row, prompt="tikket1@kali")
    t.gen_typing_text(
        "\x1b[92m# 1264 commits | 409K+ lines | 44 repos\x1b[0m",
        row,
        contin=True,
    )
    t.gen_text("", row, count=100, contin=True)

    t.gen_gif()


if __name__ == "__main__":
    main()
