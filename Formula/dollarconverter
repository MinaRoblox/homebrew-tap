class Dollarconverter < Formula
  desc "Simple tool to convert USD to MXN pesos using an online API."
  homepage "https://github.com/MinaRoblox/homebrew-tap/tree/main/sourcecode/dollarConversion"
  url "https://github.com/MinaRoblox/homebrew-tap/releases/download/dollarConversionApp/dollar"
  version "1.0.0"
  sha256 "0772616364042692bc95897bb899a5a014f376b4d2de1b141df5935d639d2988"
  license "MIT"

  depends_on :macos

  def install
    bin.install "dollar"
  end

  test do
    system "#{bin}/dollar", "--help"
  end
end
