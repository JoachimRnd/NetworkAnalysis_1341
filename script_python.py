import pyshark
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def process_capture_file(filename, display_filter):
    total_bytes = 0
    with pyshark.FileCapture(filename, display_filter=display_filter) as capture:
        for packet in capture:
            total_bytes += int(packet.captured_length)
    return total_bytes

audio_bytes = process_capture_file("discord_call_20s.pcapng", "udp")
webcam_bytes = process_capture_file("discord_call_webcam_20s.pcapng", "udp")
sharing_bytes = process_capture_file("discord_call_sharing_screen.pcapng", "udp")

call_types = ["Audio Only", "Webcam", "Screen Sharing"]
total_bytes = [audio_bytes, webcam_bytes, sharing_bytes]

plt.bar(call_types, total_bytes)
plt.title("Total Data Transmitted for Discord Calls")
plt.xlabel("Call Type")
plt.ylabel("Total Bytes")
plt.show()
