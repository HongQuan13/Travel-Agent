interface WebSocketOptions {
  reconnectInterval?: number;
  maxReconnectAttempts?: number;
}

export class AutoReconnectWebSocket {
  private url: string;
  private reconnectInterval: number;
  private maxReconnectAttempts: number;
  private currentReconnectAttempts: number = 0;
  private isManuallyClosed: boolean = false;
  private ws: WebSocket | null = null;
  public onMessage: ((msg: string) => void) | null = null;

  constructor(url: string, options: WebSocketOptions = {}) {
    this.url = url;
    this.reconnectInterval = options.reconnectInterval || 1000;
    this.maxReconnectAttempts = options.maxReconnectAttempts || Infinity;

    this.initWebSocket();
  }

  private initWebSocket(): void {
    this.ws = new WebSocket(this.url);

    this.ws.onopen = (event: Event) => {
      console.log("WebSocket connected:", event);
      this.currentReconnectAttempts = 0; // Reset attempts on successful connection
    };

    this.ws.onmessage = (message: MessageEvent) => {
      console.log("WebSocket message received:", message.data);
      if (this.onMessage) {
        this.onMessage(message.data);
      }
    };

    this.ws.onclose = (event: CloseEvent) => {
      console.warn("WebSocket closed:", event);
      if (
        !this.isManuallyClosed &&
        this.currentReconnectAttempts < this.maxReconnectAttempts
      ) {
        this.retryConnection();
      }
    };

    this.ws.onerror = (error: Event) => {
      console.error("WebSocket error:", error);
      this.ws?.close();
    };
  }

  private retryConnection(): void {
    this.currentReconnectAttempts++;
    console.log(
      `Reconnecting... (${this.currentReconnectAttempts}/${this.maxReconnectAttempts})`
    );
    setTimeout(() => {
      this.initWebSocket();
    }, this.reconnectInterval);
  }

  public send(message: string): void {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(message);
    } else {
      console.error("WebSocket is not open. Unable to send message:", message);
    }
  }

  public close(): void {
    this.isManuallyClosed = true;
    this.ws?.close();
    console.log("WebSocket manually closed.");
  }

  public isConnected(): boolean {
    return this.ws?.readyState === WebSocket.OPEN;
  }
}
