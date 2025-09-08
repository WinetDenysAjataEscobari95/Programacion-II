public class Circulo2D {
    // Campos privados
    private double x;
    private double y;
    private double radio;

    public Circulo2D() {
        this.x = 0;
        this.y = 0;
        this.radio = 1;
    }

    public Circulo2D(double x, double y, double radio) {
        this.x = x;
        this.y = y;
        this.radio = radio;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getRadio() {
        return radio;
    }

    public double getArea() {
        return Math.PI * radio * radio;
    }

    public double getPerimetro() {
        return 2 * Math.PI * radio;
    }

    public boolean contiene(double px, double py) {
        double distancia = Math.sqrt(Math.pow(this.x - px, 2) + Math.pow(this.y - py, 2));
        return distancia <= radio;
    }

    public boolean contiene(Circulo2D c) {
        double distanciaCentros = Math.sqrt(Math.pow(this.x - c.x, 2) + Math.pow(this.y - c.y, 2));
        return distanciaCentros + c.radio <= this.radio;
    }

    public boolean sobrepone(Circulo2D c) {
        double distanciaCentros = Math.sqrt(Math.pow(this.x - c.x, 2) + Math.pow(this.y - c.y, 2));
        return distanciaCentros < this.radio + c.radio;
    }

    public static void main(String[] args) {
        Circulo2D c1 = new Circulo2D(2, 0, 1);

        System.out.println("Área: " + c1.getArea());
        System.out.println("Perímetro: " + c1.getPerimetro());
        System.out.println("¿Contiene el punto (2.5, 0)? " + c1.contiene(2.5, 0));
        System.out.println("¿Contiene el círculo (2, 0, 0.5)? " + c1.contiene(new Circulo2D(2, 0, 0.5)));
        System.out.println("¿Se sobrepone con el círculo (0, 0, 2)? " + c1.sobrepone(new Circulo2D(0, 0, 2)));
    }
}
