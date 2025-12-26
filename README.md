# ComfyUI Google AI Studio Node

[English](#english) | [中文](#chinese)

---

## English

### Introduction

This is a custom node for ComfyUI that integrates Google AI Studio's Gemini 3 Pro Image API (also known as Nano Banana Pro) to enable text-to-image and image-to-image workflows.

### Features

- **Text-to-Image Generation**: Generate images from text prompts using Google's Gemini 3 Pro Image model
- **Image-to-Image Generation**: Use existing images as reference to generate new images
- **Multiple Image Inputs**: Supports up to 10 image inputs (Gemini 3 Pro Image supports up to 14 images)
- **Batch Generation**: Generate multiple images in one workflow
- **Configurable Parameters**: Full control over generation parameters including:
  - Temperature (0.0 - 2.0)
  - Aspect Ratio (1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
  - Resolution (1K, 2K, 4K)
  - Number of images to generate (1-10)
  - Google Search integration (enabled/disabled)
- **Real-time Status Feedback**: Displays execution progress in the console
- **Proxy Support**: Built-in proxy support for network environments requiring proxy

### Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone or copy this repository:
   ```bash
   git clone https://github.com/Hifunyo/comfyui_google_ai.git
   ```

3. Install required dependencies:
   ```bash
   cd comfyui_google_ai
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

**Note:** The API key input field will automatically display as a password field (showing asterisks) for security. The actual API key is only used internally and is not exposed in the console output (only a masked version is shown).

### Usage

#### Getting API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy your API key

#### Text-to-Image Workflow

1. Add the **GoogleAIGenerateImage** node to your workflow
2. Enter your API key in the `api_key` field (it will be displayed as asterisks for security)
3. Enter your text prompt in the `prompt` field
4. Configure parameters:
   - `temperature`: Controls randomness (default: 1.0)
   - `aspect_ratio`: Image aspect ratio (default: 9:16)
   - `resolution`: Output resolution (default: 2K)
   - `num_images`: Number of images to generate (default: 1)
   - `google_search`: Enable Google Search (default: false)
5. Execute the workflow

#### Image-to-Image Workflow

1. Add the **GoogleAIGenerateImage** node to your workflow
2. Connect an input image to the `init_image` input
3. Enter your API key and prompt
4. Configure parameters as needed
5. Execute the workflow

### Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `prompt` | STRING | Text description of the image to generate | Required |
| `api_key` | STRING | Google AI Studio API key (displayed as asterisks) | Required |
| `model` | STRING | Model to use (gemini-3-pro-image-preview) | gemini-3-pro-image-preview |
| `temperature` | FLOAT | Controls randomness (0.0-2.0) | 1.0 |
| `aspect_ratio` | STRING | Image aspect ratio | 9:16 |
| `resolution` | STRING | Output resolution (1K, 2K, 4K) | 2K |
| `num_images` | INT | Number of images to generate (1-10) | 1 |
| `google_search` | BOOLEAN | Enable Google Search | false |
| `init_image` | IMAGE | Optional input image for image-to-image | Optional |

**Security Note:** The API key input field is displayed as a password field (showing asterisks) to protect your credentials. The console output also shows only a masked version of the key.

### Proxy Configuration

If you need to use a proxy, set the following environment variables:

```bash
set HTTP_PROXY=http://proxy.example.com:port
set HTTPS_PROXY=http://proxy.example.com:port
```

Or configure proxy in your system settings.

### Troubleshooting

**Q: "API Key is required" error**
A: Make sure you have entered a valid API key in the `api_key` field.

**Q: Connection timeout errors**
A: Check your network connection and configure proxy if necessary.

**Q: "Media resolution is not enabled for this model" error**
A: This error should not occur with the current implementation. If it does, please check that you're using the correct model (gemini-3-pro-image-preview).

**Q: Images not generating**
A: Check the console output for detailed error messages and ensure your API key has sufficient quota.

### License

This project is licensed under the MIT License.

### Credits

- Built for ComfyUI
- Uses Google AI Studio's Gemini 3 Pro Image API
- Inspired by the need for high-quality AI image generation in ComfyUI workflows

---

## 中文

### 简介

这是一个用于 ComfyUI 的自定义节点，集成了 Google AI Studio 的 Gemini 3 Pro Image API（也称为 Nano Banana Pro），可以实现文生图和图生图的工作流。

### 功能特性

- **文生图生成**：使用 Google 的 Gemini 3 Pro Image 模型根据文本提示生成图像
- **图生图生成**：使用现有图像作为参考生成新图像
- **多图像输入**：支持最多 10 个图像输入（Gemini 3 Pro Image 支持最多 14 张图像）
- **批量生成**：在一个工作流中生成多张图像
- **可配置参数**：完全控制生成参数，包括：
  - 温度（0.0 - 2.0）
  - 宽高比（1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9）
  - 分辨率（1K, 2K, 4K）
  - 生成图像数量（1-10）
  - Google 搜索集成（启用/禁用）
- **实时状态反馈**：在控制台显示执行进度
- **代理支持**：内置代理支持，适用于需要代理的网络环境

### 安装

1. 导航到您的 ComfyUI custom_nodes 目录：
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. 克隆或复制此仓库：
   ```bash
   git clone https://github.com/Hifunyo/comfyui_google_ai.git
   ```

3. 安装所需的依赖项：
   ```bash
   cd comfyui_google_ai
   pip install -r requirements.txt
   ```

4. 重启 ComfyUI

**注意：** API 密钥输入框会自动显示为密码框（显示星号）以确保安全。实际的 API 密钥仅在内部使用，不会在控制台输出中暴露（仅显示脱敏版本）。

### 使用方法

#### 获取 API 密钥

1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建新的 API 密钥
3. 复制您的 API 密钥

#### 文生图工作流

1. 将 **GoogleAIGenerateImage** 节点添加到您的工作流中
2. 在 `api_key` 字段中输入您的 API 密钥（为了安全，它会显示为星号）
3. 在 `prompt` 字段中输入您的文本提示
4. 配置参数：
   - `temperature`：控制随机性（默认：1.0）
   - `aspect_ratio`：图像宽高比（默认：9:16）
   - `resolution`：输出分辨率（默认：2K）
   - `num_images`：要生成的图像数量（默认：1）
   - `google_search`：启用 Google 搜索（默认：false）
5. 执行工作流

#### 图生图工作流

1. 将 **GoogleAIGenerateImage** 节点添加到您的工作流中
2. 将输入图像连接到 `init_image` 输入
3. 输入您的 API 密钥和提示
4. 根据需要配置参数
5. 执行工作流

### 参数说明

| 参数 | 类型 | 描述 | 默认值 |
|------|------|------|--------|
| `prompt` | STRING | 要生成的图像的文本描述 | 必填 |
| `api_key` | STRING | Google AI Studio API 密钥（显示为星号） | 必填 |
| `model` | STRING | 要使用的模型（gemini-3-pro-image-preview） | gemini-3-pro-image-preview |
| `temperature` | FLOAT | 控制随机性（0.0-2.0） | 1.0 |
| `aspect_ratio` | STRING | 图像宽高比 | 9:16 |
| `resolution` | STRING | 输出分辨率（1K, 2K, 4K） | 2K |
| `num_images` | INT | 要生成的图像数量（1-10） | 1 |
| `google_search` | BOOLEAN | 启用 Google 搜索 | false |
| `init_image` | IMAGE | 可选的输入图像，用于图生图 | 可选 |

**安全提示：** API 密钥输入框显示为密码框（显示星号）以保护您的凭据。控制台输出也仅显示密钥的脱敏版本。

### 代理配置

如果您需要使用代理，请设置以下环境变量：

```bash
set HTTP_PROXY=http://proxy.example.com:port
set HTTPS_PROXY=http://proxy.example.com:port
```

或者在您的系统设置中配置代理。

### 故障排除

**Q: "API Key is required" 错误**
A: 确保您在 `api_key` 字段中输入了有效的 API 密钥。

**Q: 连接超时错误**
A: 检查您的网络连接，并在必要时配置代理。

**Q: "Media resolution is not enabled for this model" 错误**
A: 当前实现不应出现此错误。如果出现，请检查您是否使用了正确的模型（gemini-3-pro-image-preview）。

**Q: 图像未生成**
A: 检查控制台输出以获取详细的错误消息，并确保您的 API 密钥有足够的配额。

### 许可证

本项目采用 MIT 许可证。

### 致谢

- 为 ComfyUI 构建
- 使用 Google AI Studio 的 Gemini 3 Pro Image API
- 受 ComfyUI 工作流中高质量 AI 图像生成需求的启发

---

## Links

- **GitHub Repository**: https://github.com/Hifunyo/comfyui_google_ai
- **Google AI Studio**: https://makersuite.google.com/app/apikey
- **Gemini API Documentation**: https://ai.google.dev/gemini-api/docs/gemini-3?hl=zh-cn
- **Image Generation Documentation**: https://ai.google.dev/gemini-api/docs/image-generation?hl=zh-cn

## Support

For issues and questions, please visit the [GitHub Issues](https://github.com/Hifunyo/comfyui_google_ai/issues) page.