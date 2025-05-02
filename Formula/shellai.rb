class Shellai < Formula
    desc "Simple utility to use the google-generativeai in the CLI. Has not been tested in Linux."
    homepage "https://github.com/MinaRoblox/shellAI"
    url "https://github.com/MinaRoblox/shellAI/releases/download/Main/shellai"
    version "1.0.0"
    sha256 "2c9d326e8d732aeb1ddaf7732a52078e1e25087c01a57c940602e5922ea82a28"
    license "MIT"
  
    depends_on :macos
  
    def install
      bin.install "shellai"
    end
  
    test do
      system "#{bin}/shellai", "--help"
    end
  end
  