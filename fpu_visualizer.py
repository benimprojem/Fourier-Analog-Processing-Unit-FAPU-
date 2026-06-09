import numpy as np
import matplotlib.pyplot as plt

def run_and_visualize_fpu(inputs, weights, base_freq=1e9):
    """
    FPU Saf Sinüs Girişim Çekirdeği Simülasyonu ve Görselleştirici.
    
    inputs: Giriş vektörü (Genlik değerleri)
    weights: Matris ağırlıkları (Radyan cinsinden Faz Kaymaları)
    base_freq: Ana taşıyıcı frekans (Varsayılan 1 GHz)
    """
    # Zaman ekseni: 1 GHz dalganın 2 periyodunu inceleyelim (2 nanosaniye)
    t = np.linspace(0, 2e-9, 1000) 
    
    individual_waves = []
    super_wave = np.zeros_like(t)
    
    # 1. Çekirdekteki her bir giriş kanalının dalga üretimi (DDS)
    for i, (amp, phase) in enumerate(zip(inputs, weights)):
        # Fiziksel Saf Sinüs Formülü: V = A * sin(2*pi*f*t + phi)
        wave = amp * np.sin(2 * np.pi * base_freq * t + phase)
        individual_waves.append(wave)
        
        # 2. Pasif Direnç Ağında Fiziksel Girişim (Kirchhoff Toplamı)
        super_wave += wave 
        
    # --- GRAFİKSEL GÖRSELLEŞTİRME KATMANI ---
    plt.style.use('dark_background') # Kurumsal ve teknolojik bir görünüm için karanlık tema
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    fig.suptitle('FPU (Fourier Processing Unit) Analog Computational Core\nDesigned by DissConnecTed', fontsize=14, fontweight='bold', color='#00ffcc')

    # Üst Grafik: Çekirdeğe Giren Bağımsız Sinüs Dalgaları
    colors = ['#ff0055', '#00ff55', '#0055ff', '#ffaa00']
    for i, wave in enumerate(individual_waves):
        ax1.plot(t * 1e9, wave, label=f'Kanal {i+1} (Genlik: {inputs[i]}, Faz: {weights[i]:.2f} rad)', 
                 color=colors[i % len(colors)], alpha=0.8, linewidth=1.5)
    
    ax1.set_title('1. Aşama: Giriş Hafızasından (IMEM) Üretilen 1 GHz Saf Sinüs Dalgaları', fontsize=11, color='#abcdef')
    ax1.set_ylabel('Voltaj (V)', color='#abcdef')
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.legend(loc='upper right', fontsize=8)

    # Alt Grafik: Çekirdek Çıkışındaki Girişim (Hesaplama Çıktısı)
    ax2.plot(t * 1e9, super_wave, color='#00ffcc', linewidth=2.5, label='Çıkış Süper Dalgası (O(1) Sonuç)')
    
    # Maksimum yapıcı girişimi (hesaplama sonucunu) işaretleyelim
    max_idx = np.argmax(np.abs(super_wave))
    ax2.scatter(t[max_idx] * 1e9, super_wave[max_idx], color='white', s=50, zorder=5)
    ax2.annotate(f' ADC Örnekleme Noktası\n V_max = {super_wave[max_idx]:.3f}V', 
                 xy=(t[max_idx] * 1e9, super_wave[max_idx]), color='white', fontsize=9,
                 arrowprops=dict(arrowstyle="->", color='white'))

    ax2.set_title('2. Aşama: Pasif Çekirdekte Oluşan Girişim (Anlık Dalga Toplamı)', fontsize=11, color='#abcdef')
    ax2.set_xlabel('Zaman (Nanosaniye)', color='#abcdef')
    ax2.set_ylabel('Voltaj (V)', color='#abcdef')
    ax2.grid(True, linestyle='--', alpha=0.3)
    ax2.legend(loc='upper right', fontsize=10)

    plt.tight_layout()
    
    # Grafiği kaydet (GitHub README dosyasında göstermek için harika olur)
    plt.savefig('fpu_interference_graph.png', dpi=300)
    print("[FPU] Grafik başarıyla oluşturuldu ve 'fpu_interference_graph.png' olarak kaydedildi.")
    plt.show()

if __name__ == "__main__":
    # Test Verileri: Yapay zeka katmanından gelen örnek girişler ve matris ağırlıkları
    # Giriş genlikleri (Voltaj çarpanları)
    ornek_girisler = [1.2, 0.8, 1.5, 0.5] 
    
    # Ağırlık matrisinin oluşturduğu faz kaymaları (Radyan)
    ornek_agirliklar = [0.0, np.pi/3, np.pi/2, np.pi] 
    
    # Simülasyonu ve görselleştirmeyi çalıştır
    run_and_visualize_fpu(ornek_girisler, ornek_agirliklar, base_freq=1e9)