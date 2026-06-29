import socket
import whisper

print("Loading Whisper Model Once...")

# Whisper's internal model downloader uses urllib with NO timeout set.
# If your network can connect but then stalls (common with some VPNs,
# corporate networks, or firewalls that silently drop packets instead
# of rejecting them), this would previously hang forever with zero
# error message. Setting a global socket timeout makes it fail loudly
# instead, so you actually see what's wrong.
socket.setdefaulttimeout(60)

try:
    # device="cpu" forced explicitly: on machines without a CUDA GPU
    # (e.g. Macs), letting torch auto-detect can behave inconsistently.
    model = whisper.load_model("base", device="cpu")
    print("Whisper Ready!")
except socket.timeout:
    raise RuntimeError(
        "Whisper model download timed out after 60s. This usually means "
        "your network/firewall/VPN is blocking or silently dropping the "
        "connection to openaipublic.azureedge.net. Try: (1) a different "
        "network, (2) disabling VPN, or (3) manually downloading the "
        "model once on a network that works."
    )
except Exception as e:
    raise RuntimeError(f"Failed to load Whisper model: {e}")


def generate_transcript(audio_file, transcript_file):

    result = model.transcribe(audio_file)

    transcript = result["text"]

    with open(transcript_file, "w", encoding="utf-8") as f:

        f.write(transcript)

    return transcript
